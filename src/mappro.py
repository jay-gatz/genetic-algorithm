import random

def generate_map(level_len=random.randint(63, 103)):
    p_map = '_'
    map_elems = ['_', 'G', 'L', 'M']
    while len(p_map) < level_len:
        p_map += random.choice(map_elems)
        while p_map[-2:] == 'GG' or p_map[-2:] == 'GL' or p_map[-2:] == 'LG':
            p_map = p_map[:-1]
            p_map += random.choice(map_elems)
    return p_map

if __name__ == '__main__':
    print(generate_map())