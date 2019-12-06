
# Advent of Code Day 6 solution - https://adventofcode.com/2019/day/6

# ACTUAL DATA
# I give up with the big input strings, just dump to file and read from now on.
def _read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

input_data = [n.strip('\r') for n in _read_file('input/day_6_input.txt').split('\n')]

# TEST DATA

# input_data = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN'] # 54 orbits, 4 orbital transfers

# each body directly orbits only one other body - record this in a dict which we can then use to calculate orbit chains
direct_orbits = dict([(child, parent) for parent, child in [o.split(')') for o in input_data]])

def path_to_root(this_body, direct_orbits):
    """Follow a chain of orbits back down to the root body."""
    path = []
    # if this_body is not in the list of keys for direct_orbits then it orbits nothing and we're at the root
    while this_body in direct_orbits:
        path.append(this_body)
        this_body = direct_orbits[this_body]
    # append the root
    path.append(this_body)
    return path

# total orbits is the sum of the length of the path to root for each body in the system, minus the root body
# since it orbits nothing itself
print(sum([len(path_to_root(body, direct_orbits)[:-1])  for body in direct_orbits]))

def path_to_santa(direct_orbits):
    """Calculate the path to Santa!"""
    # we can get the path to santa by following the path to root down, and then turning around 
    # at the first intersection and following the path back up to santa
    you_path_to_root = path_to_root('YOU', direct_orbits)[1:]
    san_path_to_root = path_to_root('SAN', direct_orbits)[1:]
    intersection = list(set(you_path_to_root) & set(san_path_to_root))
    first_common = intersection[0]
    return list(set(you_path_to_root) ^ set(intersection)) + [first_common] + list(set(san_path_to_root) ^ set(intersection))[::-1]

# orbit transfers counts A -> B -> C as two transfers, so subtract one from our path list to get transfer number
print(len(path_to_santa(direct_orbits)) - 1)
