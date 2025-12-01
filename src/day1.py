import utils;

puzzle_input = utils.read_example_input(
    """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
)

puzzle_input = utils.read_puzzle_input("inputs/input1.txt")

def main():
    zeros = 0
    acc = 50
    for line in puzzle_input:
        op, num = line[0], int(line[1:])
        
        # How often do we turn a full circle?
        zeros += (num // 100)
        num = num % 100

        if op == "L":
            # do we cross 0 from the right?
            zeros += (num >= acc and acc > 0)
            acc -= num
        else:
            # do we cross 0 from the left?
            zeros += (num >= (100-acc))
            acc += num

        acc = acc % 100

    print(zeros)

if __name__ == "__main__":
    main()
