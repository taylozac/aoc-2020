
# Get data
data = []

f = open("input.txt", "r")
for line in f:
    data.append(int(line.strip("\n")))
f.close()

val1 = 0
val2 = 0

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] + data[j] == 2020:
            val1 = data[i]
            val2 = data[j]
    else:
        continue
    break

print(val1)
print(val2)

print(val1 * val2)
