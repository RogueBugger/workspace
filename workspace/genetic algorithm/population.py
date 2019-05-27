from dna import *


class Population:
    def __init__(self,mutationRate, maxpop, target):
        self.mutationRate=mutationRate
        self.target=target
        self.maxpop=maxpop
        self.population=[]
        for _ in range(maxpop):
            self.population.append(Dna(len(target)))
        self.matingPool=[]
        self.calcFitness()


    def calcFitness(self):
        for pop in self.population:
            pop.calcFitness(self.target)
            print(pop.gene, pop.fitness,end = "")