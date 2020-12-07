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
        child = [child[2: child.index(" bag")], int(child[0])]

        # Store the children
        rules[parent].append(child)

################################################################################
def rec_rules(key):

    # IF we've already calculated nubmer of sub bags, just return that value.
    if key in visited:
        return visited[key]

    # If there are no sub bags, memoize it and return 0.
    if rules[key] == None:
        visited[key] = 0
        return 0

    # Count number of sub bags.
    visited[key] = 0
    for sub in rules[key]:

        # Get number of sub bags.
        res = rec_rules(sub[0])

        # If the sub bag has no other bags, just add the number of that bag we
        # have. Otherwise, add the number of sub bags times the number of bags
        # of that type that we have, then add the number of those bags (memoize
        # values as we go).
        if res == 0:
            visited[key] += sub[1]
        else:
            visited[key] += res * sub[1] + sub[1]

    return visited[key]

###############################################################################

# Get the number of sub bags for "shiny gold"
print(rec_rules("shiny gold"))
