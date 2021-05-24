import random
from game import *


class GeneticAlgo():
    def __init__(self, initial_pop=263, cross_over_num=1, cross_over_pos1=3,
                 cross_over_pos2=6, mutation_prob=0.1, selection_type=0, fitness_win=False):
        self.initial_pop = initial_pop
        self.cross_over_pos1 = cross_over_pos1
        self.cross_over_pos2 = cross_over_pos2
        self.mutation_prob = mutation_prob
        self.selection_type = selection_type
        self.fitness_win = fitness_win
        self.cross_over_num = cross_over_num
        self.population = {}

    def fitness_function(self):
        pass

    def create_initial_population(self):
        pass

    def cross_over(self):
        pass

    def mutation(self):
        pass

    def step(self):
        pass
