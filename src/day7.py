import utils


def main():
    puzzle_input = utils.read_example_input(
""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input7.txt")

    grid = [list(line) for line in puzzle_input]
    h, w = utils.input_dim(grid)

    # Count the total number of splits for part 1.
    part1_splits = 0

    # Track the paths that led us to a beam being at pos (i,j) for part 2.
    split_path_counts = {(i,j): 0 for i in range(h) for j in range(w)}

    for i in range(1, h):
        for j in range(w):
            # Splits can come from beams until here or from beams just split onto this position.
            path_count_until_here = split_path_counts[i-1, j] + split_path_counts[i, j]

            # Beam goes into a splitter
            if grid[i][j] == "^" and grid[i-1][j] in {"S", "|"}:
                part1_splits += 1
                grid[i][j-1] = "|"
                grid[i][j+1] = "|"

                # We split for the first time.
                if path_count_until_here == 0:
                    path_count_until_here = 1

                # The split adds to paths that are adjacent.
                split_path_counts[i, j-1] += path_count_until_here
                split_path_counts[i, j+1] += path_count_until_here
            # Beam continues on
            elif grid[i-1][j] in {"S", "|"}:
                grid[i][j] = "|"

                # No new path added, just propagate the existing count.
                split_path_counts[i, j] = path_count_until_here

    split_timelines = sum(split_path_counts[h-1, j] for j in range(w))


    print(part1_splits)
    print(split_timelines)



if __name__ == "__main__":
    main()
