import re

# Define a new function that could return the positions of the first nucleotide at restriction cutting sites.
def cut_sites(sequence,restriction):

    # Find all cutting sites. 
    matches=re.finditer(f'(?={restriction})',sequence)
    
    # Define an empty list to store the positions of cutting sites and add them to the list one by one.
    result=[]
    for i in matches:
        result.append(i.start()+1)
    return result

# Request the user to input the DNA sequence and restriction enzyme cutting sequence.
DNA_sequence=input('DNA_sequence:')
restriction_sequence=input('restriction_sequence:')

# Output the positions of the first nucleotide at restriction cutting sites.
a=cut_sites(DNA_sequence,restriction_sequence)
print(a)

