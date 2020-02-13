from individual import Individual
import random


class Generation:

    index = 0

    def __init__(self, size, gene_length, age=0):
        self.individuals = [Individual(gene_length) for i in range(size)]
        self.size = size
        self.age = age
        self.name = "Generation " + str(age)
        Generation.index = Generation.index + 1
        self.gene_length = gene_length
        self.sort()

    def sort(self):
        for i in range(self.size):
            for j in range(i+1, self.size):
                if self.individuals[i].get_score() < self.individuals[j].get_score():
                    aux = self.individuals[i]
                    self.individuals[i] = self.individuals[j]
                    self.individuals[j] = aux

    def __str__(self):
        return self.name + " " + str(self.individuals[0])

    def do_generations(self, number):
        next_generation = self.get_next_generation()
        for i in range(number-1):
            next_generation = next_generation.get_next_generation()
        return next_generation

    def get_next_generation(self):
        keep_limit = len(self.individuals) // 10
        next_generation = Generation(len(self.individuals), self.gene_length, self.age+1)
        for i in range(keep_limit):
            next_generation.set_individual(i, self.individuals[i])
        for i in range(keep_limit, len(self.individuals)):
            parent_a = self.individuals[random.randrange(0, self.size // 2)]
            parent_b = self.individuals[random.randrange(0, self.size // 2)]
            next_generation.set_individual(i, parent_a.breed(parent_b))
        next_generation.sort()
        return next_generation

    def set_individual(self, index, individual):
        if index < len(self.individuals):
            self.individuals[index] = individual

    def get_individual(self, index):
        if index < len(self.individuals):
            return self.individuals[index]
        return None
