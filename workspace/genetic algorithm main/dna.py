from random import randint
import math,random


def newChar():
    r = randint(63, 122)  
    #r = 32 if r == 63 else randint(63, 122)
    r = 32 if r == 63 else r
   
    r = 46 if r == 64 else r
    return chr(r)

class Dna: 
    def __init__(self, len):
        self.gene=[]
        for _ in range(len):
            self.gene.append(newChar())

        self.fitness=0

    def calcFitness(self, target):
        score = 0
        for i in range(len(self.gene)):
            if self.gene[i] == target[i]:
                score +=1
        self.fitness = (score / len(target)) ** 8
        #self.fitness = (score / len(target))

    def crossOver(self, partner):
        child = Dna(len(partner.gene))
        midpoint = random.randint(0, len(partner.gene))
        #midpoint = math.floor(len(partner.gene)/2)
        for i in range(len(self.gene)):
            child.gene[i] = self.gene[i] if i > midpoint else partner.gene[i]
        
        return child

    def mutation(self, mutationRate):
        for e in range(len(self.gene)):
            if random.random() < mutationRate:
                self.gene[e] = newChar() 