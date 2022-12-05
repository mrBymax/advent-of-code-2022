from utils.api import get_input

input_str = get_input(4)
lines = input_str.splitlines()

ans = 0

for line in lines:
    first_pair, second_pair = line.split(',')
    sector1, elf1 = first_pair.split('-')
    sector2, elf2 = second_pair.split('-')

    sector1, elf1, sector2, elf2 = [int(x) for x in [sector1, elf1, sector2, elf2]]

    # first part
    # if s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1:
    #     print(s1, e1, s2, e2)
    #     ans += 1

    # second part
    if elf1 >= sector2 and elf2 >= sector1:
        ans += 1

print(ans)
