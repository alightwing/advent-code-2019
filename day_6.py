
# Advent of Code Day 6 solution - https://adventofcode.com/2019/day/6

# ACTUAL DATA
# I give up with the big input strings, just dump to file and read from now on.
def _read_file(filename):
	with open(filename, 'r') as f:
		return f.read()

input_data = [n.strip('\r') for n in _read_file('input/day_6_input.txt').split('\n')]

# TEST DATA

# input_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'] # 42 orbits
# input_data = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN'] # 4 orbital transfers

direct_orbits = {}

# each body directly orbits only one other body
# record this in a dict which we can then use to calculate orbit chains
for orbit in input_data:
	parent, child = orbit.split(')')
	direct_orbits[child] = parent

def path_to_root(start_body, direct_orbits):
	"""Follow a chain of orbits back down to the root body."""
	path = []
	this_body = start_body
	while True:
		path.append(this_body)
		# if this_body is not in the list of keys for direct_orbits then it orbits nothing
		# and we've reached the end of the chain - break
		if this_body not in direct_orbits:
			break
		this_body = direct_orbits[this_body]
	return path

# total orbits is the sum of the length of the path to root for each body in the system, minus the root body
# since it orbits nothing itself
orbits_num = sum([len(path_to_root(body, direct_orbits)) - 1 for body in direct_orbits])
print(orbits_num)

def path_to_santa(direct_orbits):
	"""Calculate the path to Santa!"""
	# we can get the path to santa by following the path to root down, and then turning around 
	# at the first intersection and following the path back up to santa
	you_path_to_root = path_to_root('YOU', direct_orbits)
	san_path_to_root = path_to_root('SAN', direct_orbits)
	# get the intersection
	intersection = list(set(you_path_to_root) & set(san_path_to_root))
	# get the first common body in each path - this is where we turn around and is part of the path
	# otherwise we remove the rest of our common bodies from our transfer path
	first_common = intersection[0]
	# construct our path in a somewhat convoluted way
	path = [b for b in you_path_to_root if b not in intersection] + [first_common]
	path += list(reversed([b for b in san_path_to_root if b not in intersection]))
	# remove the 'YOU' at the start and the 'SAN' at the end
	path = path[1:-1]
	return path

shortest_path = path_to_santa(direct_orbits)
# orbit transfers counts A -> B -> C as two transfers, so subtract one from our path list to get transfer number
print(len(shortest_path) - 1)
