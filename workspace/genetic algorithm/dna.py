from random import randint
from math import ceil
def newChar():
    r = randint(63, 122)  
    r = 32 if r == 63 else randint(63, 122)
    r = 46 if r == 64 else randint(63, 122)
    return chr(r)

class Dna:
    def __init__(self, len):
        self.gene=[]
        for _ in range(len):
            self.gene.append(newChar())

        self.fitness=0

    def calcFitness(self,target):
        score=0
        for e in self.gene:
            if e in target:
                score+=1
        self.fitness= ceil(score / len(target))
