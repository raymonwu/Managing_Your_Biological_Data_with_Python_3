'''

Simulate Mendelian inheritance of pea strains.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 11.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

class Pea:

    def __init__(self, genotype):
        self.genotype = genotype

    def get_phenotype(self):
        if "G" in self.genotype:
            return "yellow"
        else:
            return "green"

    def create_offspring(self, other):
        offspring = []
        new_genotype = ""
        for haplo1 in self.genotype:
            for haplo2 in other.genotype:
                new_genotype = haplo1 + haplo2
                offspring.append(Pea(new_genotype))
        return offspring

    def get_tab_separated_text(self):
        return '%s\t%s' % (self.genotype, self.get_phenotype())

    # def __repr__(self):
    #     return self.get_phenotype() + ' [%s]' % self.genotype

    def __repr__(self):
        return '(%s)' % self.genotype + '-----' + self.get_phenotype()

yellow = Pea("GG")
# print(yellow.genotype)
# print(yellow.get_phenotype())
# print(yellow)

green = Pea("gg")
# print(green.genotype)
# print(green.get_phenotype())
# print(green)

# GG * gg
f1 = yellow.create_offspring(green)
# print(f1[0])
# print(f1[1])

# Gg * Gg
f2 = f1[0].create_offspring(f1[1])
print(f1)
print(f2)

for pea in f2:
    print(pea.get_tab_separated_text())