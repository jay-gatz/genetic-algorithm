import random
import itertools
from game import *


class GeneticAlgo:
    def __init__(self, p_map, initial_pop_num=200, cross_over_type=0, cross_over_pos1=3,
                 cross_over_pos2=6, mutation_prob=0.1, selection_type=0, selection_num=10,
                 fitness_win=False):
        self.p_map = p_map
        self.map_len = len(p_map)
        self.initial_pop_num = initial_pop_num
        self.cross_over_type = cross_over_type
        self.cross_over_pos1 = cross_over_pos1
        self.cross_over_pos2 = cross_over_pos2
        self.mutation_prob = mutation_prob
        self.selection_type = selection_type
        self.selection_num = selection_num
        self.fitness_win = fitness_win
        self.population = {}
        self.steps = 0
        self.done = False

    # Function that Calculate the Fitness Function for the Solution!
    def fitness_function(self, solution):
        # Create Game Object with the Input Map!
        g = Game([self.p_map])
        # Load the Game Level!
        g.load_next_level()
        # Calculate the Solution!
        return g.get_score(solution)

    # Function that Create the Initial Population Randomly!
    def create_initial_pop(self):
        # Create Initial Population Number of Solutions!
        for i in range(self.initial_pop_num):
            first_time = True
            solution = None
            # Make Random Solution while its Going to be New!
            while solution in self.population or first_time:
                first_time = False
                solution = ''
                while len(solution) < self.map_len:
                    solution += str(random.randint(0, 2))
                    # The Solution Should not Have Following Jumps!
                    if solution[-1] == '1' and len(solution) < self.map_len - 1:
                        solution += '0'
            # Add the Solution to the Population!
            self.population[solution] = self.fitness_function(solution)

    # Selection Phase!
    def selection(self):
        selected_parents = list(self.population.keys())
        # Selection Type #0 !
        # Make the Best Solutions (Half of the Population that Sorted by the Fitness Func)
        if self.selection_type == 0:
            selected_parents = selected_parents[:len(selected_parents) // 2]
        # Selection Type #1 !
        # Make the Best Solutions (Random Choice with probability of the Fitness Func)
        else:
            selected_parents = random.choices(self.population,
                                              weights=self.population.values())
        return selected_parents

    # CrossOver Phase!
    def cross_over(self, selected_parents):
        # Define Child Solutions List!
        child_solutions = []
        # Create Selection Number Children with Crossover!
        for i in range(self.selection_num):
            # Choose 2 Parents from Solutions that Selected in the Selection Phase!
            parent1 = random.choice(selected_parents)
            parent2 = random.choice(selected_parents)
            # CrossOver Type #0
            # Parent #0 [0 ... CrossOver Pos 1] | Parent #2 [CrossOver Pos 1 ... End]
            if self.cross_over_type == 0:
                child = parent1[:self.cross_over_pos1] + parent2[self.cross_over_pos1:]
            # CrossOver Type #1
            # Parent #0 [0 ... CrossOver Pos 1]  | Parent #2 [CrossOver Pos 1 ... CrossOver Pos 2] | Parent #0 [CrossOver Pos 2 ... End]
            else:
                child = parent1[:self.cross_over_pos1] + \
                        parent2[self.cross_over_pos1:self.cross_over_pos2] + \
                        parent2[self.cross_over_pos2:]
            # Append Created Solution to the Child Solutions List!
            child_solutions.append(child)
        return child_solutions

    # Mutation Phase!
    def mutation(self, childs):
        # Check the Probability and Value and Mutate if The Condition is True!
        for i, child in enumerate(childs):
            if random.uniform(0, 1) < self.mutation_prob:
                child = list(child)
                # Change Random Step of the Solution to the JUMP Action!
                child[random.randint(0, len(child) - 1)] = '1'
                childs[i] = ''.join(child)
        return childs

    # Create the Next Generation!
    def step(self):
        # Sort Population Dictionary by the Fitness Function!
        self.population = dict(sorted(self.population.items(), key=lambda item: item[1]
                                      , reverse=True))
        print(self.population)
        # Do the Selection Phase!
        selected_parents = self.selection()
        # Do the CrossOver Phase!
        child_solutions = self.cross_over(selected_parents)
        # Do the Mutation Phase!
        child_solutions = self.mutation(child_solutions)
        for child_solution in child_solutions:
            self.population[child_solution] = self.fitness_function(child_solution)
        # Print the Mean of the Generation's Fitness Function!
        print(sum([p[1] for p in self.population.values()]) / len(self.population))

    # Run the Genetic Algorithm !
    def run(self):
        # Create the Initial Population!
        self.create_initial_pop()
        # Do While the Algorithm is not Done!
        while not self.done:
            # Make the Next Generation!
            self.step()
            input()
        # Return the Solution! :D
        self.solution = self.population[0]
        return self.solution
