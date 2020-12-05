f = open("input.txt", "r")
raw = f.read().splitlines();
f.close()

data = []

for i in range(len(raw)):
    data.append([raw[i][:7], raw[i][7:]])

max_id = -1

for seat in data:

    row = 0;
    col = 0;

    for i in range(7):
        if seat[0][i] == "B":
            row += (2 ** (6 - i))

        if i < 3:
            if seat[1][i] == "R":
                col += (2 ** (2 - i))

    seat_id = (row * 8) + col

    if seat_id > max_id:
        max_id = seat_id

print(max_id)
