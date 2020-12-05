import string

# Check if a given string is an int.
def is_int():
    pass

# Define a function that checks if a passport is valid.
def is_valid(passport, reqs):

    # Check for all required fields.
    for req in reqs:
        if req not in passport:
            return False

    # If we are here we have all the required fields. Now we will check that
    # the requirements of each field are correct.

    # Further process the data.
    passport = passport.split(" ")
    passport.pop()
    passport.sort()
    if "cid" in passport[1]:
        passport.pop(1)
    passport = [elem[4:] for elem in passport]


    # Order of data:
    # [byr, ecl, eyr, hcl, hgt, iyr, pid]

    # Check byr.
    byr = 1920 <= int(passport[0]) <= 2002
    print("byr", passport[0], byr)

    # Check ecl.
    color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = passport[1] in color
    print("ecl", passport[1], ecl)

    # Check eyr.
    eyr = 2020 <= int(passport[2]) <= 2030
    print("eyr", passport[2], eyr)

    # Check hcl.
    valid_chars = string.hexdigits[:-6]
    hcl = True
    for c in passport[3][1:]:
        if c not in valid_chars:
            hcl = False
            break
    hcl = passport[3][0] == "#" and hcl
    print("hcl", passport[3], hcl)

    # Check hgt.
    hgt = False
    if passport[4][-2:] == "cm":
        hgt = 150 <= int(passport[4][:-2]) <= 193
    elif passport[4][-2:] == "in":
        hgt = 59 <= int(passport[4][:-2]) <= 76
    print("hgt", passport[4], hgt)

    # Check iyr.
    iyr = 2010 <= int(passport[5]) <= 2020
    print("iyr", passport[5], iyr)

    # Check pid.
    pid = len(passport[6]) == 9 and passport[6].isdigit()
    print("pid", passport[6], pid)

    #return True

    # If all conditions are true, return true.
    return byr and ecl and eyr and hcl and hgt and iyr and pid

################################################################################

# Get the data.
f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()

# Definitions of used variables.
data = []
req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
curr_pass = ""
valid = 0

# Process our raw data into a useable format.
for partial in raw:

    # Skip appending cid data.
    #if 'cid' in partial:
    #    continue

    # Appending the current data and a space (for my sanity) to the current
    # passport.
    curr_pass += partial + " "


    # If we have found the delineator betweem passports, append the newly
    # completed passport and reset the string we append to.
    if partial == '':
        data.append(curr_pass[:-1])
        curr_pass = ""


# Check if each candidate passowrd is valid and count it if it is.
for cand in data:
    if is_valid(cand, req_fields):
        valid += 1

print(valid)

#for d in data:
#    print(d)

#print(raw)
