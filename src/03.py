from utils.api import get_input

input_str = get_input(3)
lines = input_str.splitlines()

ans = 0
i = 0


def score(common_char):
    if 'a' <= common_char <= 'z':
        return ord(common_char) - ord('a') + 1
    else:
        return ord(common_char) - ord('A') + 1 + 26


while i < len(lines):
    for c in lines[i]:
        if c in lines[i + 1] and c in lines[i + 2]:
            ans += score(c)
            break
    i += 3

print(ans)

# first part

for lines in open('inputs/03'):
    lines = lines.strip()
    first_half, second_half = lines[:len(lines) // 2], lines[len(lines) // 2:]
    for c in first_half:
        if c in second_half:
            pass
