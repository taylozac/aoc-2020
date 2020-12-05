data = []

f = open("input.txt", "r")
for line in f:
    line = line.strip("\n").split(" ")
    line = [int(line[0].split("-")[0]), int(line[0].split("-")[1]), line[1][0], line[2]]
    data.append(line)

valid = 0
for password in data:
    count = 0
    for i in range(len(password[3])):
        if password[3][i] == password[2]:
            count += 1
    if count in range(password[0], password[1] + 1):
        valid += 1
        print(password)

print(valid)
