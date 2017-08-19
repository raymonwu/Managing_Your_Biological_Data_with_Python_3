'''
Count the occurrence of each amino acid in a protein sequence

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 2.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

# insulin [Homo sapiens] GI:386828
# extracted 51 amino acids of A+B chain
insulin = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
in_my = "SJJAKDJAKNCNZMNCNAIUEQIJDAKLMCZNBADIOEQ8RIIOOKALQZ"

for amino_acid in "ACDEFGHIKLMNPQRSTVWY":
    number = insulin.count(amino_acid)
    print (amino_acid, number)

# Test
print('\n')
for letter in "ABCDEFG":
    number_my = in_my.count(letter)
    print (letter,number_my)