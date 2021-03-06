from dna import *
import math,random



def translate(value, leftmin, leftmax, rightmin, rightmax):
    leftspan = leftmax - leftmin
    rightspan = rightmax - rightmin

    valueScaled = float(value - leftmin) / float(leftspan)
    return (rightmin + (valueScaled * rightspan))


def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y


class Population:
    def __init__(self,mutationRate, maxpop, target):
        self.mutationRate=mutationRate
        self.target=target
        self.maxpop=maxpop
        self.population=[]
        for _ in range(maxpop):
            self.population.append(Dna(len(target))) 
        self.matingPool=[]
        self.best=""
        self.generation = 0
        self.finished = False
        self.average_fitness = 0
        self.calcFitness()

    def calcFitness(self):
        for pop in self.population:
            pop.calcFitness(self.target)

           

    def reproduction(self):
        fit=[]
        for pop in self.population:
            fit.append(pop.fitness)
        maxfitness=max(fit)

        
        for pop in self.population:
            for _ in range(math.floor(translate(pop.fitness, 0, maxfitness, 0, 1)*100)):
                self.matingPool.append(pop)
               
    def generate(self):
        for pop in range(len(self.population)):
            parent1=random.randint(0,(len(self.matingPool)-1))
            parent2=random.randint(0,(len(self.matingPool)-1))
            partnerA = self.matingPool[parent1]
            partnerB = self.matingPool[parent2]
            child = partnerA.crossOver(partnerB)
            child.mutation(self.mutationRate)
            self.population[pop] = child

        self.generation += 1

    def evaluate(self):
        index = 0
        maxfitness = 0
        for pop in range(len(self.population)):
            if self.population[pop].fitness > maxfitness:
                maxfitness = self.population[pop].fitness  
                index = pop
        tring = ""
        self.best = tring.join(self.population[index].gene)
        
        if maxfitness == 1:
            self.finished = True

    def fitnesss(self):
        total = 0
        for pop in range(len(self.population)):
            total =  self.population[pop].fitness

        return (total / len(self.population))

