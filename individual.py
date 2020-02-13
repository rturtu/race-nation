from gene import Gene
import random
from fitness import Fitness
import string


class Individual:

    def __init__(self, gene_length):
        self.gene_length = gene_length
        # Constructor for a random individual
        self.genes = [Gene() for i in range(gene_length)]
        self.name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        self.compute_fitness()

    def copy(self, individual):
        for i in range(self.gene_length):
            self.genes[i].copy(individual.get_gene(i))

    def get_gene_length(self):
        return self.gene_length

    def __str__(self):
        return self.name + " " + str(self.get_score())

    def get_gene(self, index):
        if len(self.genes) > index:
            return self.genes[index]
        return Gene()

    def set_gene(self, gene, index):
        if len(self.genes) > index:
            self.genes[index] = gene

    def breed(self, individual):
        max_gene_length = None
        if individual.gene_length < self.gene_length:
            max_gene_length = self.gene_length
        else:
            max_gene_length = individual.gene_length
        new_individual = Individual(max_gene_length)
        parent_a = self
        parent_b = individual
        # Random chance to swap parents
        if random.random() < 0.5:
            aux = parent_a
            parent_a = parent_b
            parent_b = aux

        new_individual.copy(parent_a)
        gene_joint1 = random.randint(0, parent_b.get_gene_length() - 1)
        gene_joint2 = parent_b.get_gene_length()
        for i in range(gene_joint1, gene_joint2):
            action = parent_b.get_gene(i)
            new_individual.set_gene(action, i)
        new_individual.mutate()
        new_individual.compute_fitness()
        return new_individual

    def get_score(self):
        return self.fitness.get_score()

    def compute_fitness(self):
        self.fitness = Fitness(self)

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.01:
                gene.mutate()
