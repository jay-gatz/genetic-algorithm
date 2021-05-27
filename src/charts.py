from statistics import *
from matplotlib import pyplot

class PPlot:
    def __init__(self, fitness_history):
        self.fitness_history = fitness_history

    def calculate_pm(self):
        self.max_f = []
        self.min_f = []
        self.mean_f = []
        for fitness_list in self.fitness_history:
            self.max_f.append(max(fitness_list))
            self.min_f.append(min(fitness_list))
            self.mean_f.append(mean(fitness_list))

    def show_plots(self):
        self.calculate_pm()
        pyplot.plot(self.max_f)
        pyplot.plot(self.min_f)
        pyplot.plot(self.mean_f)
        pyplot.show()
