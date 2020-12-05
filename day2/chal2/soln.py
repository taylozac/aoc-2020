data = []

f = open("input.txt", "r")
for line in f:
    line = line.strip("\n").split(" ")
    line = [int(line[0].split("-")[0]), int(line[0].split("-")[1]), line[1][0], line[2]]
    data.append(line)

valid = 0
for password in data:
    idx1 = password[0] - 1
    idx2 = password[1] - 1

    res1 = 0
    if password[3][idx1] == password[2]:
        res1 = 1

    res2 = 0
    if password[3][idx2] == password[2]:
        res2 = 1

    if res1 ^ res2 == 1:
        valid += 1
        print(password)

print(valid)
