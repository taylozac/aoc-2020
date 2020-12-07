import string

f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()


data = []
group = ""
for person in raw:

    if person == "":
        data.append(group)
        group = ""
        continue

    group += person

data.append(group)

yes = 0
for group in data:
    for letter in string.ascii_lowercase:
        if letter in group:
            yes += 1

print(yes)
