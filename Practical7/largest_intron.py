import re

# Input the sequence
seq ='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Find the longest sequence that meets the conditions and calculate its length.
intron=re.findall(r'GT.+AG',seq)
length=len(intron[0])
print(length)
