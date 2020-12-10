f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()

boot = []
for instr in raw:
    instr = instr.split(" ")
    boot.append([instr[0], int(instr[1])])


def terminates(instr):
    acc = 0
    ip = 0
    ran = []

    while True:

        if ip >= len(boot):
            return True, acc

        if ip in ran:
            return False,acc

        ran.append(ip)

        if instr[ip][0] == "nop":
            ip += 1
        elif instr[ip][0] == "jmp":
            ip += boot[ip][1]
        else:
            acc += boot[ip][1]
            ip += 1


swap = {"jmp": "nop", "nop": "jmp"}
for i in boot:

    if i[0] == "acc":
        continue

    i[0] = swap[i[0]]

    if i[0] != "jmp" or i[1] != 0:
        res, acc = terminates(boot)

        if res:
            print(acc)
            break

    i[0] = swap[i[0]]
