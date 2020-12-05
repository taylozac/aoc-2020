################################################################################
# Solve the problem for given info

def num_trees(vert_stride, horiz_stride, height, width, data):

    horiz_pos = 0
    tree_count = 0

    for i in range(0, height, vert_stride):
        if data[i][horiz_pos] == '#':
            tree_count += 1
        horiz_pos = (horiz_pos + horiz_stride) % width

    return tree_count

################################################################################
# Get the data

data = []

f = open("input.txt", "r")
for line in f:
    data.append(line.strip("\n"))
f.close()

width = len(data[0])
height = len(data)

################################################################################
# Compute results

results = []

results.append(num_trees(1, 1, height, width, data))
results.append(num_trees(1, 3, height, width, data))
results.append(num_trees(1, 5, height, width, data))
results.append(num_trees(1, 7, height, width, data))
results.append(num_trees(2, 1, height, width, data))

mult_res = 1;
for res in results:
    mult_res *= res

print(mult_res)
