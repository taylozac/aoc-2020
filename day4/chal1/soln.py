# Define a function that checks if a passport is valid.
def is_valid(passport, reqs):

    # Check for all required fields.
    for req in reqs:
        if req not in passport:
            return False
    return True

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
