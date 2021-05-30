from src.algos import *
from src.charts import *
from src.render import *
from src.mappro import *

if __name__ == '__main__':
    if input('Open Map or Generate a Random Map? (0:Open, 1:Random)    ') == '0':
        file = open(f'../levels/level{input("Level Number?    ")}.txt')
        p_map = file.readline()
    else:
        p_map = generate_map()

    selection_type = eval(input(f'Selection Type? (0: 1/2, 1: Weigh Rand)    '))
    cross_over_type = eval(input(f'CrossOver Type? (0: 1P, 1: 2P)    '))
    cross_over1 = eval(input(f'CrossOver1 Pos ({len(p_map)}) ?   '))
    cross_over2 = 63
    if cross_over_type == 1:
        cross_over2 = eval(input(f'CrossOver2 Pos ({len(p_map)}) ?   '))
    g = GeneticAlgo(p_map, cross_over_pos1=cross_over1, cross_over_pos2=cross_over2,
                    selection_type=selection_type, cross_over_type=cross_over_type,
                    initial_pop_num=200, selection_num=100, mutation_prob=0.5,
                    mutation_num=6)
    solution, fitness_history = g.run()

    pplot = PPlot(fitness_history)
    pplot.show_plots()

    visualizer = Visualize(p_map, solution[0])
    visualizer.render()
