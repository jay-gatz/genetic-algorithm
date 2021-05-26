from src.algos import *
from src.charts import *
from src.render import *

if __name__ == '__main__':
    file = open(f'../levels/level{input("Level Number?    ")}.txt')
    # file = open(f'levels/level{10}.txt')
    map = file.readline()
    selection_type = eval(input(f'Selection Type? (0: 1/2, 1: Weigh Rand)    '))
    cross_over_type = eval(input(f'CrossOver Type? (0: 1P, 1: 2P)    '))
    cross_over1 = eval(input(f'CrossOver1 Pos ({len(map)}) ?   '))
    cross_over2 = 63
    if cross_over_type == 1:
        cross_over2 = eval(input(f'CrossOver2 Pos ({len(map)}) ?   '))
    g = GeneticAlgo(map, cross_over_pos1=cross_over1, cross_over_pos2=cross_over2,
                    selection_type=selection_type, cross_over_type=cross_over_type,
                    initial_pop_num=200, selection_num=100)
    solution, fitness_history = g.run()

    # pplot = PPlot(fitness_history)
    # pplot.show_plots()

    visualizer = Visualize(map, solution[0])
    visualizer.render()
