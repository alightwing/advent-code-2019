# Advent of Code Day 4 solution - https://adventofcode.com/2019/day/4

def _adjacency(counter, num_consecutives):
	if num_consecutives:
		return counter == num_consecutives
	return counter >= 1

def check_conditions(num, num_consecutives=0):
	num_list = [int(n) for n in list(str(num))]
	last_num = num_list[0]
	consecutive_counter = 0
	adjacency = False
	for this_num in num_list[1:]:
		# check that the numbers are ascending and instantly return False if not
		if this_num < last_num:
			return False
		# if we haven't found the adjacency condition, do the adjacency check
		if not adjacency:
			if this_num == last_num:
				consecutive_counter += 1
			else:
				adjacency = _adjacency(consecutive_counter, num_consecutives)
				consecutive_counter = 0
		last_num = this_num
	return adjacency or _adjacency(consecutive_counter, num_consecutives)

# source_iter = [111111, 122345, 123789, 122346, 112233, 123444, 111122]
source_iter = range(123257, 647016)
valid = [n for n in source_iter if check_conditions(n, num_consecutives=1)]
print(len(valid))
