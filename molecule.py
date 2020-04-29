
class Molecule:
    def __init__(self, elements, amounts):
        self.molecule = dict(zip(elements, amounts))
    def __str__(self):
        return "".join([str(a)+str(self.molecule[a]) for a in self.molecule])
