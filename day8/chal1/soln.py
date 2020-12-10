f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()

boot = []
for instr in raw:
    instr = instr.split(" ")
    boot.append([instr[0], int(instr[1])])


acc = 0
ip = 0
ran = []

while True:

    if ip in ran:
        break

    ran.append(ip)

    if boot[ip][0] == "nop":
        ip += 1
    elif boot[ip][0] == "jmp":
        ip += boot[ip][1]
    else:
        acc += boot[ip][1]
        ip += 1


print(acc)
