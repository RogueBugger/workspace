if  __name__ == "__main__":
    from population import Population

    target = 'to be or not to be'
    maxpop = 200
    mutation_rate = 0.01


    population = Population(mutation_rate, maxpop, target)  

    while(population.best != target):
        population.calcFitness()
        population.reproduction()
        population.generate()
        population.evaluate()
        #print(population.generation)
        print(population.best)