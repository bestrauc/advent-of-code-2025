import itertools

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

import utils


def find_min_button_combination(target: np.array, button_masks: np.array) -> int:
    m = len(button_masks)
    for k in range(1, m+1):
        for selected_buttons in itertools.combinations(range(m), k):
            selected_masks = button_masks[selected_buttons, :]
            xored = np.logical_xor.reduce(selected_masks)

            if np.array_equal(xored, target):
                return k

    raise AssertionError("One should work?")

def find_min_button_joltage(joltages: np.array, button_masks: np.array) -> int:
    n_vars = len(button_masks)

    # Define (b1*x + b2*y + b3*z + .. = [j1, j2, ..]) as a integer
    # programming problem with integer variables to minimize.

    # Minimize x + y + z + .., i.e. the sum of button presses.
    c = np.ones(n_vars, dtype=int)  
    # We set lower and upper bound the same, i.e. we want equality.
    constraints = LinearConstraint(button_masks.T, joltages, joltages)
    # Set integrality to 1 for all variables, to make it integer.
    integrality = np.ones(n_vars, dtype=int)
    # Non-negative variables only.
    bounds = Bounds(lb=0, ub=np.inf)

    result = milp(c, constraints=constraints, integrality=integrality, bounds=bounds)
    return int(result.fun)

def main():
    puzzle_input = utils.read_example_input(
"""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input10.txt")

    inputs = []
    for line in puzzle_input:
        target, *buttons, joltages = line.split()
        target = np.array([(c == "#") for c in target.strip("[]")])
        buttons = [list(map(int, b.strip("()").split(","))) for b in buttons]

        # Conver the [0,2] button format to a mask like [True, False, True, False]
        button_masks = []
        for button in buttons:
            mask = np.zeros_like(target, dtype=bool)
            mask[button] = True
            button_masks.append(mask)

        button_masks = np.stack(button_masks)

        joltages = np.array(list(map(int, joltages.strip("{}").split(","))))

        inputs.append((target, button_masks, joltages))


    button_sum = 0
    joltage_sum = 0
    for target, button_masks, joltages in inputs:
        min_buttons = find_min_button_combination(target, button_masks)
        button_sum += min_buttons

        min_joltage_buttons = find_min_button_joltage(joltages, button_masks)
        joltage_sum += min_joltage_buttons

    print(button_sum)
    print(joltage_sum)

if __name__ == "__main__":
    main()
