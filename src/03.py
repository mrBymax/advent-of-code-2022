from utils.api import get_input

input_str = get_input(3)
line = input_str.split('\n')

ans = 0
i = 0


def score(common_char):
    if 'a' <= common_char <= 'z':
        return ord(common_char) - ord('a') + 1
    else:
        return ord(common_char) - ord('A') + 1 + 26


while i < len(line):
    for c in line[i]:
        if c in line[i + 1] and c in line[i + 2]:
            ans += score(c)
            break
    i += 3

print(ans)

# first part

for line in open('inputs/03'):
    line = line.strip()
    first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
    for c in first_half:
        if c in second_half:
            pass
