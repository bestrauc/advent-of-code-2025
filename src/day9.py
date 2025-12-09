import itertools

import numpy as np
from shapely import Polygon

import utils


def area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return (abs(p1[0] - p2[0]) + 1)*(abs(p1[1] - p2[1]) + 1)

def is_in_polygon(poly: Polygon, p1: tuple[int, int], p2: tuple[int, int]) -> bool:
    p3 = (p1[0], p2[1])
    p4 = (p2[0], p1[1])

    # Check if the rectangle is contained in the specified polygon.
    rect = Polygon([p1, p3, p2, p4])
    return poly.contains(rect)

def main():
    puzzle_input = utils.read_example_input(
"""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input9.txt")

    arr = [tuple(map(int,line.split(","))) for line in puzzle_input]
    poly = Polygon(list(arr))

    max_area1 = 0
    max_area2 = 0
    for p1, p2 in itertools.combinations(arr, 2):
        max_area1 = max(area(p1, p2), max_area1)
        if is_in_polygon(poly, p1, p2):
            max_area2 = max(area(p1, p2), max_area2)

    print(max_area1)
    print(max_area2)


if __name__ == "__main__":
    main()
