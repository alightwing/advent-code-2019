# Advent of Code Day 7 solution - https://adventofcode.com/2019/day/57
# This one went horribly wrong and I settled for a garbage solution that nevertheless produces the right answers. Will fix later.

import itertools

# ACTUAL DATA

raw_program = "3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99"

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

def opcode_3(program, pointer_pos, input_value):
    # hardcoded input_value is a hack but don't need to do more right now
    program[program[pointer_pos + 1]] = input_value
    pointer_pos += 2
    return program, pointer_pos

def opcode_4(program, pointer_pos):
    param_modes = get_param_modes(program[pointer_pos], 1)
    output = get_param(program, pointer_pos + 1, param_modes[0])
    pointer_pos += 2
    return program, pointer_pos, output

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

def run_program(program, inputs, pointer_pos=0):
    while True:
        opcode = get_opcode(program[pointer_pos])
        # 99 is end of program
        if opcode == 99:
            break
        if opcode == 3:
            program, pointer_pos = opcode_3(program, pointer_pos, inputs.pop(0))
        elif opcode == 4:
            program, pointer_pos, output = opcode_4(program, pointer_pos)
            return output, pointer_pos
        else:
            opcode_func = eval('opcode_{}'.format(opcode))
            program, pointer_pos = opcode_func(program, pointer_pos)

def check_phase_setting(program, setting):
    output = 0
    for input_val in setting:
        program_iter = program.copy()
        output = run_program(program_iter, [input_val, output])[0]
    return output

# raw_program = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"

input_program = [int(n) for n in raw_program.split(',')]

phase_settings = itertools.permutations(range(5))

outputs = {}

for setting in phase_settings:
    outputs[check_phase_setting(input_program, setting)] = setting

max_output = max(outputs.keys())
print(max_output)
print(outputs[max_output])

phase_settings = itertools.permutations(range(5, 10))

outputs = {}

for setting in phase_settings:
    programstore = [(input_program.copy(), 0) for n in range(5)]
    output = 0
    for index, input_val in enumerate(setting):
        this_program, pointer_pos = programstore[index]
        output, pointer_pos = run_program(this_program, [input_val, output], pointer_pos)
        programstore[index] = (this_program, pointer_pos)
    while True:
        if programstore[4][0][programstore[4][1]] == 99:
            break
        for index in range(5):
            this_program, pointer_pos = programstore[index]
            output, pointer_pos = run_program(this_program, [output], pointer_pos)
            programstore[index] = (this_program, pointer_pos)
    outputs[output] = setting

max_output = max(outputs.keys())
print(max_output)
print(outputs[max_output])
