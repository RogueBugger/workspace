if  __name__ == "__main__":
    from population import Population
   

    target = 'fuck the world population maxpop'
    maxpop = 10000
    mutation_rate = 0.01


    population = Population(mutation_rate, maxpop, target)  
   
    while(population.finished!=True):
        population.calcFitness()
        population.reproduction()
        population.generate()
        population.calcFitness()
        population.evaluate()
        print(population.best,population.generation)
      