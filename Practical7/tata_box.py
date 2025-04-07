import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input:
    gene_name=''
    sequence=''
    with open('tata_genes.fa','w') as output:
        for line in input:
            line=line.strip()
            if line.startswith('>'):
                if re.search(r'TATA[AT]A[AT]',sequence):
                    output.write('>'+gene_name+'\n')
                    output.write(sequence+'\n')
                gene_name=re.findall(r'gene:(\S+)',line)[0]
                sequence=''
            else:
                sequence+=line
        if re.search(r'TATA[AT]A[AT]',sequence):
            output.write('>'+gene_name+'\n')
            output.write(sequence+'\n')