bases = ['A','C','T','G']
seq = 'CAGGCCATTRKGL'
for i in seq:
    if i not in bases:
        print(i,"is not a nucleotide")