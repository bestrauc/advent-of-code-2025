import itertools

from termcolor import colored

import utils


def repeated_once(num: str) -> bool:
    n = len(num)
    return num[:n//2] == num[n//2:]

def repeated_at_least_twice(num: str) -> bool:
    n = len(num)
    for i in range(1, n // 2 + 1):
        # Just split into batches of length N and see if they are all equal.
        repeats = set(itertools.batched(num, i))
        if len(repeats) == 1:
            return True

    return False

def main():
    puzzle_input = (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
        "824824821-824824827,2121212118-2121212124"
    )
    puzzle_input = open("inputs/input2.txt").read()
    ranges = [tuple(map(int, part.split("-"))) for part in puzzle_input.split(",")]

    acc = 0
    for a,b in ranges:
        silly_numbers = []
        for i in range(a,b+1):
            if repeated_at_least_twice(str(i)):
                silly_numbers.append(i)

        acc += sum(silly_numbers)
        print(f"{a}-{b}: {colored(silly_numbers, 'red')}")

    print(acc)

if __name__ == "__main__":
    main()
