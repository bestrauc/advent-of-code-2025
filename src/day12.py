import numpy as np

import utils

def main():
    puzzle_input = utils.read_example_input(
"""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input12.txt")
    *shapes, regions = utils.split_list_at(puzzle_input, pat="")

    shape_arrays = []
    for i, shape in enumerate(shapes):
        arr = np.array([[c == "#" for c in line] for line in shape[1:]], dtype=bool)
        shape_arrays.append(arr)

    not_impossible = 0
    for region in regions:
        extent, *shape_counts = region.split()
        shape_counts = list(map(int, shape_counts))
        w, h = list(map(int, extent[:-1].split("x")))
        box_area = w*h
        
        # Just check whether it could even possibly fit.
        shape_area = sum([arr.sum()*c for arr, c in zip(shape_arrays, shape_counts)])
        if shape_area <= box_area:
            not_impossible +=1 

    # Just tried it in the blind hope that the elements might tightly
    # pack together and this ended up actually being the solution.
    print(not_impossible)

if __name__ == "__main__":
    main()
