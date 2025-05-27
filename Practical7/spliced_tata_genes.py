import re

# Request the user to input a splice donor/acceptor combination and determine whether it is one of the three combinations.
choices=['GTAG','GCAG','ATAC']
choice=input(f'chosen splice donor/acceptor combinations:')
if not choice in choices:
    print('please enter again')
else:

    # Open the input file and enter read mode.
    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input_file:
        
        # Define the variables.
        gene_name=''
        sequence=''
        splice_donor=choice[0:2]
        splice_acceptor=choice[2:]

        # Open the output file and enter write mode.
        with open(f'{choice}_spliced_genes.fa','w') as out_file:   
            for line in input_file:
                
                # Remove line breaks.
                line=line.strip()

                # Locate the next gene, and then determine whether the previous gene meets the conditions.
                if line.startswith('>'):
                    if re.search(r'TATA[AT]A[AT]',sequence) and re.search(f'{splice_donor}.+{splice_acceptor}',sequence):
                        
                        # Calculate the numbers of TATA box instances and write the gene names, numbers and sequences into the output file.
                        tata_count=len(re.findall(r'TATA[AT]A[AT]',sequence))
                        out_file.write('>'+gene_name+'_'+f'{tata_count}'+'\n')
                        out_file.write(sequence+'\n')
                    
                    # Select the next gene and clear the sequence.
                    gene_name=re.findall(r'gene:(\S+)',line)[0]
                    sequence=''
                else:
                    sequence+=line
            
            # Determine whether the last gene meets the conditions.
            if re.search(r'TATA[AT]A[AT]',sequence) and re.search(f'{splice_donor}.+{splice_acceptor}',sequence):
                tata_count=len(re.findall(r'TATA[AT]A[AT]',sequence))
                out_file.write('>'+gene_name+'_'+f'{tata_count}'+'\n')
                out_file.write(sequence+'\n')