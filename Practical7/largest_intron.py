import re
seq ='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron=re.findall(r'GT.+AG',seq)
length=len(intron[0])
print(length)
