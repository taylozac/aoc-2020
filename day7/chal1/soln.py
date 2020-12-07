# Get raw data.
f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()

# Inititialize rules and visited.
rules = {}
visited = {}

# Processing the data so it is useable
for rule in raw:

    # Split parent bag from it's children
    split = rule.split(" contain ")

    # Retrieve the color of the parent.
    parent = split[0][:split[0].index(" bag")]

    # Split the children apart.
    raw_children = split[1].split(", ")

    # Create list of possible sub bags.
    rules[parent] = []
    for child in raw_children:

        # If this bag cannot contain any other bags, set its rule to None.
        if child == "no other bags.":
            rules[parent] = None
            break

        # Split the child from it's number and the trailing "bag" info.
        child = child[2: child.index(" bag")]

        # Store the children
        rules[parent].append(child)

################################################################################
def rec_rules(key):

    '''
    # This code here counts the number of ways that a bag can contain it. This
    # is from my original misinterpretation of the problem.

    if key in visited:
        return visited[key]

    if rules[key] == None:
        visited[key] = 0
        return 0

    total = 0
    for sub in rules[key]:
        total += rec_rules(sub)

    if total == 0:
        visited[key] = 0
    else:
        visited[key] = 1

    return visited[key]
    '''

    # If we've already memoized the value, just return it.
    if key in visited:
        return visited[key]

    # If a bag can't contain any other bags, return False and store that value.
    if rules[key] == None:
        visited[key] = False
        return False

    # If we have our target bag, return true.
    if key == "shiny gold":
        return True

    # Check all the sub bags and see if they can contain a bag. If one can,
    # memoize True and return it, otherwise, we memoize False and return it.
    for sub in rules[key]:
        if rec_rules(sub):
            visited[key] = True
            return True

    visited[key] = False
    return False

###############################################################################

# Count the number of bags that can eventually contain a shiny gold bag.
res = 0
visited["shiny gold"] = True
for rule in rules:
    if rec_rules(rule):
        res += 1

# For default case of shiny gold.
res -= 1

print(res)
