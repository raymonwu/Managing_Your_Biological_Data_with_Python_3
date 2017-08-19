'''

Convert a table from a nested list to a nested dictionary and back.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 7.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

table = [
    ['protein', 'ext1', 'ext2', 'ext3'],
    [0.16, 0.038, 0.044, 0.040],
    [0.33, 0.089, 0.095, 0.091],
    [0.66, 0.184, 0.191, 0.191],
    [1.00, 0.280, 0.292, 0.283],
    [1.32, 0.365, 0.367, 0.365],
    [1.66, 0.441, 0.443, 0.444]
    ]

# convert nested list to nested dict
nested_dict = {}
n = 0
key = table[0]
# to include the header , run the for loop over
# All table elements (including the first one)
for row in table[1:]:
    n = n + 1
    entry = {key[0]: row[0], key[1]: row[1], key[2]: row[2],
             key[3]: row[3]}
    nested_dict['row'+str(n)] = entry
# Test
# print(table[1:])
print(nested_dict)


nested_list = []
for entry in nested_dict:
    key = nested_dict[entry]
    nested_list.append([key['protein'], key['ext1'], key['ext2'],
                       key['ext3']])
print(nested_list)
