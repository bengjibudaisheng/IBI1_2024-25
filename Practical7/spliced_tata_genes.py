import re

choices=['GTAG','GCAG','ATAC']
choice=input(f'chosen splice donor/acceptor combinations:')
if not choice in choices:
    print('please enter again')
else:
    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input_file:
        gene_name=''
        sequence=''
        with open(f'{choice}_spliced_genes.fa','w') as out_file:   
            for line in input_file:
                line=line.strip()
                if line.startswith('>'):
                    if re.search(r'TATA[AT]A[AT]',sequence) and re.search(choice,sequence):
                        tata_count=len(re.findall(r'TATA[AT]A[AT]',sequence))
                        out_file.write('>'+gene_name+'_'+f'{tata_count}'+'\n')
                        out_file.write(sequence+'\n')
                    gene_name=re.findall(r'gene:(\S+)',line)[0]
                    sequence=''
                else:
                    sequence+=line
            if re.search(r'TATA[AT]A[AT]',sequence):
                out_file.write('>'+gene_name+'_'+f'{tata_count}'+'\n')
                out_file.write(sequence+'\n')





# def get_user_input():
#     choices = ['GTAG', 'GCAG', 'ATAC']
#     while True:
#         user_input = input(f"Enter one of {choices} for splice donor/acceptor combination: ")
#         if user_input in choices:
#             return user_input
#         print("Invalid input. Please try again.")

# def read_fasta(file_path):
#     sequences = {}
#     with open(file_path, 'r') as file:
#         current_name = None
#         current_seq = ""
#         for line in file:
#             line = line.strip()
#             if line.startswith('>'):
#                 if current_name:
#                     sequences[current_name] = current_seq
#                 current_name = line[1:].split()[0]
#                 current_seq = ""
#             else:
#                 current_seq += line
#         if current_name:
#             sequences[current_name] = current_seq
#     return sequences

# def find_spliced_tata_genes(sequences, splice_combination):
#     tata_box_pattern = re.compile(r'TATAWAW', re.IGNORECASE)
#     result_sequences = {}
#     for gene_name, seq in sequences.items():
#         if re.search(splice_combination, seq) and re.search(tata_box_pattern, seq):
#             tata_count = len(re.findall(tata_box_pattern, seq))
#             new_gene_name = f"{gene_name}_{tata_count}"
#             result_sequences[new_gene_name] = seq.replace('\n', '')
#     return result_sequences

# def write_fasta(sequences, output_path):
#     with open(output_path, 'w') as file:
#         for gene_name, seq in sequences.items():
#             file.write(f">{gene_name}\n{seq}\n")

# if __name__ == "__main__":
#     splice_combination = get_user_input()
#     file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
#     output_path = f"{splice_combination}_spliced_genes.fa"
#     sequences = read_fasta(file_path)
#     spliced_tata_genes = find_spliced_tata_genes(sequences, splice_combination)
#     write_fasta(spliced_tata_genes, output_path)