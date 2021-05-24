from algos import *

if __name__ == '__main__':
    file = open(f'levels/level{input("Level Number?    ")}.txt')
    map = file.readline()
    cross_over1 = eval(input(f'CrossOver Pos ({len(map)}) ?   '))
    g = GeneticAlgo(map, cross_over_pos1=cross_over1)
    g.run()
