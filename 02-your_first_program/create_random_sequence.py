'''

Create a random DNA sequence of length 10

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 2.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import random

alphabet = "AGCT"
sequence = ""
for i in range(10):
    index = random.randint(0, 3)
    # random.randint(a, b)¶
    # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    sequence = sequence + alphabet[index]
    
print(sequence)
