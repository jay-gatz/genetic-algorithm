from statistics import *
from matplotlib import pyplot

class PPlot:
    def __init__(self, fitness_history):
        self.fitness_history = fitness_history

    def calculate_pm(self):
        self.max_f = []
        self.min_f = []
        self.mean_f = []
        for key in self.fitness_history:
            self.max_f.append(max(self.fitness_history[key]))
            self.min_f.append(min(self.fitness_history[key]))
            self.mean_f.append(mean(self.fitness_history[key]))

    def show_plots(self):
        self.calculate_pm()
        pyplot.plot(self.max_f)
        pyplot.plot(self.min_f)
        pyplot.plot(self.mean_f)
        pyplot.show()
