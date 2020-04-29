from calculate import table
import calculate

#TODO: add more to Molecule class 
class Molecule:
    def __init__(self, name, elements, amounts):
        self.name = name
        self.molecule = dict(zip(elements, amounts))
        self.amounts = amounts
        self.elements = elements
        self.mass = sum([table[a]["atomic_mass"]*b for a,b in zip(elements, amounts)])
        self.compositions = calculate.compositions_from_empirical(self.elements, self.amounts)[1]

    def __str__(self):
        return self.name + " - " + ("".join([str(a)+str(self.molecule[a]) for a in self.molecule]))
    