import string

f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()


data = []
group = ""
group_size = 0
for person in raw:

    if person == "":
        data.append([group, group_size])
        group = ""
        group_size = 0
        continue

    group += person
    group_size += 1

data.append([group, group_size])

yes = 0
for group in data:
    for letter in string.ascii_lowercase:
        if group[0].count(letter) == group[1]:
            yes += 1

print(yes)
