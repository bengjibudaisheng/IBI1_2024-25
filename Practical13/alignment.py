# Import the module and obtain the blosum62 matrix.
import blosum as bl
blosum62=bl.BLOSUM(62) 

# Define a function for reading the FASTA sequence.
def read_fasta(filename):
    with open(filename,'r') as f:
        lines=f.readlines()
        sequence=''.join(line.strip() for line in lines[1:])
    return sequence.upper()

# Use this function to read three FASTA sequences.
human=read_fasta('SOD2_HUMAN.fasta')
mouse=read_fasta('SOD2_MOUSE.fasta')
random=read_fasta('random.fasta')

# Define a function for obtaining the alignment score and the percentage of identical amino acids.
def align_sequences(seq1,seq2):
    if len(seq1)!=len(seq2):
        raise ValueError("Sequences must be of equal length for global alignment.")
    alignment_score=0
    identical=0
    for amino_acid1,amino_acid2 in zip(seq1,seq2):
        alignment_score+=blosum62[amino_acid1][amino_acid2]
        if amino_acid1==amino_acid2:
            identical+=1
    percentage_identity=(identical/len(seq1))*100
    return alignment_score,percentage_identity

# Use this function to get the alignment score and percentage of identical amino acids for each of the three comparisons.
score_human_mouse,percentage_human_mouse=align_sequences(human,mouse)
score_human_random,percentage_human_random=align_sequences(human,random)
score_mouse_random,percentage_mouse_random=align_sequences(mouse,random)

# Print the alignment scores and the percentages of identical amino acids.
print(f'The alignment score for human-mouse is {score_human_mouse}, and the percentage of identical amino acids is {percentage_human_mouse}.')
print(f'The alignment score for human-random is {score_human_random}, and the percentage of identical amino acids is {percentage_human_random}.')
print(f'The alignment score for mouse-random is {score_mouse_random}, and the percentage of identical amino acids is {percentage_mouse_random}.')
