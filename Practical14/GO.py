import xml.dom.minidom
import xml.sax
from datetime import datetime

# DOM
def process_dom(file_path):
    start_time=datetime.now()
    dom=xml.dom.minidom.parse(file_path)
    terms=dom.getElementsByTagName('term')
    
    # Define a dictionary to store the namespace, name and count.
    max_counts={
        'molecular_function':{'count': 0, 'name': []},
        'biological_process':{'count': 0, 'name': []},
        'cellular_component':{'count': 0, 'name': []}
    }
    
    for term in terms:

        # Confirm the namespace.
        namespace_nodes=term.getElementsByTagName('namespace')
        namespace=namespace_nodes[0].firstChild.data.strip()
        
        # Calculate the number of 'is_a'.
        is_a_count = len(term.getElementsByTagName('is_a'))
        
        # Find the maximum count and the corresponding name(s).
        if is_a_count > max_counts[namespace]['count']:
            max_counts[namespace]['count'] = is_a_count
            term_node = term.getElementsByTagName('name')[0].firstChild.data.strip()
            max_counts[namespace]['name']=[term_node]
        elif is_a_count == max_counts[namespace]['count']:
            term_node = term.getElementsByTagName('name')[0].firstChild.data.strip()
            max_counts[namespace]['name'].append(term_node)
    
    # Calculate the time.
    dom_time=datetime.now()-start_time
    return max_counts,dom_time

# SAX
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.namespace = ""
        self.name = ""
        self.is_a_count = 0 

        # Define a dictionary to store the namespace, name and count.
        self.max_count = {
            'molecular_function': {'count': 0, 'name': []},
            'biological_process': {'count': 0, 'name': []},
            'cellular_component': {'count': 0, 'name': []}
        }

    def startElement(self, tag, attributes):
        self.current_element = tag
        
        # Perform initialization and clear the variables.
        if tag == "term":
            self.namespace = "" 
            self.name = "" 
            self.is_a_count = 0  

    def characters(self, content):
        
        # Confirm the namespace.
        if self.current_element == "namespace":
            self.namespace += content.strip()
        
        # Confirm the name.
        elif self.current_element == "name":
            self.name += content.strip()

        # Calculate the number of 'is_a'.
        elif self.current_element == "is_a":
            self.is_a_count += 1 

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.max_count:

                # Find the maximum count and the corresponding name(s).
                if self.is_a_count > self.max_count[self.namespace]['count']:
                    self.max_count[self.namespace]['count'] = self.is_a_count
                    self.max_count[self.namespace]['name']=[self.name]
                elif self.is_a_count == self.max_count[self.namespace]['count']:
                    self.max_count[self.namespace]['name'].append(self.name)
        
        self.current_element = "" 
    
def process_sax(file_path):
    start_time=datetime.now()
    handler=GOHandler()
    parser=xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    sax_time=datetime.now()-start_time
    return handler.max_count, sax_time

# Main program
def main():
    file_path = 'go_obo.xml'
    
    # DOM process
    dom_results, dom_time = process_dom(file_path)
    print("=== DOM Results ===")
    for ontology, data in dom_results.items():
        print(f"{ontology}: {data['name']} has {data['count']} is_a elements")
    print(f"DOM Time: {dom_time}\n")
    
    # SAX process
    sax_results, sax_time = process_sax(file_path)
    print("=== SAX Results ===")
    for ontology, data in sax_results.items():
        print(f"{ontology}: {data['name']} has {data['count']} is_a elements")
    print(f"SAX Time: {sax_time}\n")
    
    # Compare the time.
    print("### Performance Comparison ###")
    if dom_time < sax_time:
        print("DOM was faster.")
    else:
        print("SAX was faster.")

if __name__ == "__main__":
    main()