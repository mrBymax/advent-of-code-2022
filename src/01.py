from utils.api import get_input

input_str = get_input(1)

# open the file and save the contents in a variable
with open('inputs/01') as f:
    lines = f.readlines()

# remove the newline character from each line
lines = [line.rstrip() for line in lines]

# the list of sums
sums = []

# the current sum
current_sum = 0

# iterate over the lines
for line in lines:
    # if the line is not empty
    if line != '':
        # add the number to the sum
        current_sum += int(line)
    # if the line is empty
    else:
        # add the sum to the list
        sums.append(current_sum)
        # reset the sum
        current_sum = 0

# add the last sum
sums.append(current_sum)

# sort the list
sums.sort()

# print the top 3 sums
print(sums[-1])
print(sums[-2])
print(sums[-3])

print(sum(sums[-3:]))

