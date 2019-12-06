# Advent of Code Day 2 solution - https://adventofcode.com/2019/day/2

# TEST DATA

# raw_program = "1,0,0,0,99" # output 2,0,0,0,99
# raw_program = "2,3,0,3,99" # output 2,3,0,6,99
# raw_program = "2,4,4,5,99,0" # 2,4,4,5,99,9801
# raw_program = "1,1,1,4,99,5,6,0,99" # output 30,1,1,4,2,5,6,0,99

# ACTUAL DATA

raw_program = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0"

input_program = [int(n) for n in raw_program.split(',')]

# need to comment these lines out if testing
input_program[1] = 12
input_program[2] = 2

# Part 1

def run_program(program):
    current_pos = 0
    while True:
        # each operation is four parameters
        program_chunk = program[current_pos:current_pos+4]
        opcode = program_chunk[0]
        # opcode 99 is end of program
        if opcode == 99:
            break
        input_one = program[program_chunk[1]]
        input_two = program[program_chunk[2]]
        if opcode == 1:
            output = input_one + input_two
        elif opcode == 2:
            output = input_one * input_two
        else:
            raise AttributeError('unrecognised opcode: {}'.format(opcode))
        program[program_chunk[3]] = output
        current_pos += 4
    return program

output_program = run_program(input_program.copy())
print(output_program[0])

# Part 2

def find_noun_verb(program_base):
    # have to check all combinations 
    for noun in range(100):
        for verb in range(100):
            # make a copy for each 
            program_iter = program_base.copy()
            program_iter[1] = noun
            program_iter[2] = verb
            program_iter = run_program(program_iter)
            if program_iter[0] == 19690720:
                print('Noun: ', noun)
                print('Verb: ', verb)
                print('Product: ', noun * 100 + verb)
                return

find_noun_verb(input_program)
