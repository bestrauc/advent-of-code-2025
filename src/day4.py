import utils


def main():
    puzzle_input = utils.read_example_input(
"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input4.txt")

    grid = list(map(list, puzzle_input))
    h, w = utils.input_dim(puzzle_input)

    removed_count = 0

    # Just removing in an iterative fashion seems fast enough.
    # A merciful part 2 today, even if it's just day 4 / 12.
    while True:
        freed = set()

        for i in range(h): 
            for j in range(w):
                if grid[i][j] == ".":
                    continue

                neighbor_rolls = 0
                for di, dj in utils.ADJ8:
                    ni, nj = i + di, j + dj

                    if not (ni in range(h) and nj in range(w)):
                        continue

                    neighbor_rolls += (grid[ni][nj] == "@")

                if neighbor_rolls < 4:
                    removed_count += 1
                    freed.add((i,j))
            
        for i, j in freed:
            grid[i][j] = "."


        if len(freed) == 0:
            break


    print(removed_count)

if __name__ == "__main__":
    main()
