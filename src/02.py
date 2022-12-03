from utils.api import get_input

input_str = get_input(2)

with open('inputs/02') as f:
    lines = f.readlines()

total_points = 0

for line in lines:
    line = line.rstrip()
    print(line)

    opponent, me = line.split(' ')
    print(me, opponent)
    total_points += {'X': 0, 'Y': 3, 'Z': 6}[me]
    total_points += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                     ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                     ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}[(opponent, me)]

print(total_points)
