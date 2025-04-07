import re

# Open the input file and enter read mode.
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input:
    
    # Define the variables.
    gene_name=''
    sequence=''

    # Open the output file and enter write mode.
    with open('tata_genes.fa','w') as output:
        for line in input:
            
            # Remove line breaks.
            line=line.strip()
            
            # Locate the next gene, and then determine whether the previous gene meets the conditions.
            if line.startswith('>'):
                if re.search(r'TATA[AT]A[AT]',sequence):
                    
                    # Write the gene names and sequences into the output file.
                    output.write('>'+gene_name+'\n')
                    output.write(sequence+'\n')
                
                # Select the next gene and clear the sequence.
                gene_name=re.findall(r'gene:(\S+)',line)[0]
                sequence=''
            else:
                sequence+=line

        # Determine whether the last gene meets the conditions.
        if re.search(r'TATA[AT]A[AT]',sequence):
            output.write('>'+gene_name+'\n')
            output.write(sequence+'\n')