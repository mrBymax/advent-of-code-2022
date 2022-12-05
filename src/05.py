from utils.api import get_input

input_str = get_input(5)
lines = input_str.splitlines()

S = [
    [],
    ['S', 'P', 'H', 'V', 'F', 'G'],
    ['M', 'Z', 'D', 'V', 'B', 'F', 'J', 'G'],
    ['N', 'J', 'L', 'M', 'G'],
    ['P', 'W', 'D', 'V', 'Z', 'G', 'N'],
    ['B', 'C', 'R', 'V'],
    ['Z', 'L', 'W', 'P', 'M', 'S', 'R', 'V'],
    ['P', 'H', 'T'],
    ['V', 'Z', 'H', 'C', 'N', 'S', 'R', 'Q'],
    ['J', 'Q', 'V', 'P', 'G', 'L', 'F']
]

# S = [[], ['N', 'Z'], ['D', 'C', 'M'], ['P']]
print(S)

for line in lines:
    command = line.split()
    quantity = int(command[1])
    from_ = int(command[3])
    to_ = int(command[5])

    move = S[from_][:quantity]

    S[from_] = S[from_][quantity:]
    S[to_] = move + S[to_]

    print(quantity, from_, to_, S, move)

print(''.join([s[0] for s in S if len(s) > 0]))
