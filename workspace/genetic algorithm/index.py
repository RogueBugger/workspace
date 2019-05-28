if  __name__ == "__main__":
    from population import Population
   

    target = 'he ph'
    maxpop = 400
    mutation_rate = 0.01


    population = Population(mutation_rate, maxpop, target)  
    i=1
    k=1
    while(population.best!=target):
        population.calcFitness()
        population.reproduction()
        population.generate()
        population.evaluate()
        #print(population.generation)
        print(population.best,population.generation)
    