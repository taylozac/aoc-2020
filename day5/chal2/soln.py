f = open("input.txt", "r")
raw = f.read().splitlines();
f.close()

data = []

for i in range(len(raw)):
    data.append([raw[i][:7], raw[i][7:]])

ids = []

for seat in data:

    row = 0;
    col = 0;

    for i in range(7):
        if seat[0][i] == "B":
            row += (2 ** (6 - i))

        if i < 3:
            if seat[1][i] == "R":
                col += (2 ** (2 - i))

    ids.append((row * 8) + col)

ids.sort()

for i in range(len(ids) - 1):
    if ids[i + 1] - ids[i] == 2:
        print(ids[i+1] - 1)
        break
else:
    print("uhh this flight is full")
