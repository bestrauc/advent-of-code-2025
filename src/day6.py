import utils
import math

import numpy as np

def get_nth_digit(num: int, n: int) -> int:
    return math.remainder(num // (10**n), 10)

def get_part1_inputs(puzzle_input: list) -> list:
    math_inputs = [[int(n) for n in line.split()] for line in puzzle_input[:-1]]
    math_inputs = utils.transpose(math_inputs)
    return math_inputs

def get_part2_inputs(puzzle_input: list) -> list:
    math_inputs = [list(line) for line in puzzle_input[:-1]]
    math_inputs = utils.transpose(math_inputs)

    all_inputs = []
    next_inputs = []
    for column in math_inputs:
        # If we have a column of all spaces, we reached the end of the input.
        if all(c == " " for c in column):
            all_inputs.append(next_inputs)
            next_inputs = []
        else:
            # Otherwise join the column digits, e.g. ["3", "5", " "] -> 35
            next_inputs.append(int("".join(column)))

    if len(next_inputs) > 0:
        all_inputs.append(next_inputs)

    return all_inputs

def acc_inputs(operators: list[str], math_inputs: list[list[int]]) -> int:
    acc = 0
    for op, inputs in zip(operators, math_inputs):
        if op == "*":
            acc += math.prod(inputs)
        else:
            acc += sum(inputs)

    return acc


def main():
    puzzle_input = utils.read_example_input(
"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """,
    strip=False
    )

    puzzle_input = utils.read_puzzle_input("inputs/input6.txt", strip=False)

    problem_operators = puzzle_input[-1].split()
    
    math_inputs1 = get_part1_inputs(puzzle_input)
    math_inputs2 = get_part2_inputs(puzzle_input)

    solution1 = acc_inputs(problem_operators, math_inputs1)
    solution2 = acc_inputs(problem_operators, math_inputs2)
    
    print(solution1)
    print(solution2)


if __name__ == "__main__":
    main()
