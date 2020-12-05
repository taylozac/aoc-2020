data = []

f = open("input.txt", "r")
for line in f:
    data.append(line.strip("\n"))
f.close()

width = len(data[0])
height = len(data)

horiz_pos = 0
tree_count = 0

for i in range(height):
    if data[i][horiz_pos] == '#':
        tree_count += 1
    horiz_pos = (horiz_pos + 3) % width

print(tree_count)
