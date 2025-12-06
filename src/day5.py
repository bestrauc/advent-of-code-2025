import utils

def count_fresh_in_ranges(ranges: list[range], ingr_ids: list[int]) -> int:
    fresh = 0
    for ingr in ingr_ids:
        for r in ranges:
            if ingr in r:
                fresh += 1
                break

    return fresh

def count_range_coverage(ranges: list[range]):
    """Count the number of numbers covered by the ranges

    Idea: sort the ranges by start and stop, so they are laid out like this
        0123456789
        ---
        ----
         -----
         --------   <- here we count the range 6,7,8 as new.
          --        <- [2,3] not counted, we already counted till 8
          ---       <- [2,4] not counted, we already counted till 8
          --------  <- here the 9 is new

        So this just trivially covers 10 numbers (0 .. 9).

    And then count the numbers covered by the ranges, always starting at the max
    seen so far. For example, the highlighted ones wouldn't be counted again.
    """
    sorted_ranges = sorted(ranges, key=lambda r: (r.start, r.stop))
    
    fresh = 0
    min_start = 0
    for r in sorted_ranges:
        start_idx = max(0, min_start - r.start)
        fresh += len(r[start_idx:])

        # Move start offset if we found a new longer one.
        min_start = max(min_start, r.stop)

    return fresh


def main():
    puzzle_input = utils.read_example_input(
"""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input5.txt")
    ranges, ingr_ids = utils.split_list_at(puzzle_input, pat="")

    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    ranges = [range(a, b+1) for a,b in ranges]

    ingr_ids = [int(i) for i in ingr_ids]

    print(count_fresh_in_ranges(ranges, ingr_ids))
    print(count_range_coverage(ranges))

if __name__ == "__main__":
    main()
