# Advent of Code Day 5 solution - https://adventofcode.com/2019/day/5

# TEST DATA

# raw_program = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"

# ACTUAL DATA

raw_program = "3,225,1,225,6,6,1100,1,238,225,104,0,1,191,196,224,1001,224,-85,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,45,50,225,1102,61,82,225,101,44,39,224,101,-105,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,102,14,187,224,101,-784,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1001,184,31,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,91,18,225,2,35,110,224,101,-810,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,76,71,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,7,16,225,1102,71,76,224,101,-5396,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,72,87,225,1101,56,77,225,1102,70,31,225,1102,29,15,225,1002,158,14,224,1001,224,-224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,494,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226"

# input for our program
input_value = 5

def get_param_modes(opcode, num_params):
	"""Calculate parameter modes - 0 (position) or 1 (immediate)."""
	# if it's a single digit opcode then everything is positional
	if len(str(opcode)) == 1:
		return [0 for n in range(num_params)]
	# otherwise remove last two digits of opcode character and get modes
	else:
		param_modes = [int(n) for n in list(str(opcode)[:-2])]
		# if there are fewer modes than params, default to 0 for remaining
		while len(param_modes) < num_params:
			param_modes = [0] + param_modes
	# finally we need to reverse the modes because they come out of the opcode backwards
	return list(reversed(param_modes))

def get_param(program, param_pos, mode):
	"""Get operation param based on position and mode."""
	param = program[param_pos]
	if mode:
		return param
	else:
		return program[param]

# one function per opcode is very verbose, but I have a feeling future problems will revisit this code
# and this way it's very extensible

def _opcodes_1_2_params(program, pointer_pos):
	"""Calculate first two params for an opcode based on param mode."""
	param_modes = get_param_modes(program[pointer_pos], 2)
	input_param_one = get_param(program, pointer_pos + 1, param_modes[0])
	input_param_two = get_param(program, pointer_pos + 2, param_modes[1])
	return input_param_one, input_param_two

def opcode_1(program, pointer_pos):
	input_param_one, input_param_two = _opcodes_1_2_params(program, pointer_pos)
	program[program[pointer_pos + 3]] = input_param_one + input_param_two
	pointer_pos += 4
	return program, pointer_pos

def opcode_2(program, pointer_pos):
	input_param_one, input_param_two = _opcodes_1_2_params(program, pointer_pos)
	program[program[pointer_pos + 3]] = input_param_one * input_param_two
	pointer_pos += 4
	return program, pointer_pos

def opcode_3(program, pointer_pos):
	# hardcoded input_value is a hack but don't need to do more right now
	program[program[pointer_pos + 1]] = input_value
	pointer_pos += 2
	return program, pointer_pos

def opcode_4(program, pointer_pos):
	param_modes = get_param_modes(program[pointer_pos], 1)
	output = get_param(program, pointer_pos + 1, param_modes[0])
	print('Output: ', output)
	pointer_pos += 2
	return program, pointer_pos

def opcode_5(program, pointer_pos):
	param_one, param_two = _opcodes_1_2_params(program, pointer_pos)
	if param_one:
		pointer_pos = param_two
	else:
		pointer_pos += 3
	return program, pointer_pos

def opcode_6(program, pointer_pos):
	param_one, param_two = _opcodes_1_2_params(program, pointer_pos)
	if not param_one:
		pointer_pos = param_two
	else:
		pointer_pos += 3
	return program, pointer_pos

def opcode_7(program, pointer_pos):
	param_one, param_two = _opcodes_1_2_params(program, pointer_pos)
	program[program[pointer_pos + 3]] = int(param_one < param_two)
	pointer_pos += 4
	return program, pointer_pos

def opcode_8(program, pointer_pos):
	param_one, param_two = _opcodes_1_2_params(program, pointer_pos)
	program[program[pointer_pos + 3]] = int(param_one == param_two)
	pointer_pos += 4
	return program, pointer_pos

def get_opcode(param):
	"""Get the opcode from the opcode character."""
	if param == 99:
		return param
	return int(str(param)[-1])

def run_program(program):
	pointer_pos = 0
	while True:
		opcode = get_opcode(program[pointer_pos])
		# 99 is end of program
		if opcode == 99:
			break
		opcode_func = eval('opcode_{}'.format(opcode))
		program, pointer_pos = opcode_func(program, pointer_pos)
	return program

input_program = [int(n) for n in raw_program.split(',')]
run_program(input_program) 
