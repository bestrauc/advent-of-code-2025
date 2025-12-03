import functools

import utils

def tuple_to_dec(seq: tuple[int, ...]) -> int:
    return functools.reduce(lambda x,y: 10*x+y, seq)

@functools.cache
def max_k_subseq(seq: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Get the maximal subsequence via dynamic programming.

    The basic idea is that the maximum subsequence value follows the recursion:

    Let f(n, k) be the max value of a k-subsequence in an n-digit string. Then

        f(n, k) = max(f(n-1, k), 10*head_val + f(n-1, k-1))

    where f(n-1, k) is if you not take the leading digit and still have k options
    in the remaining n-1 length tail subsequence and f(n-1, k-1) is when you choose
    the current leading digits and only have k-1 in the tail subsequence.

    The recurrence repeats subproblems, so we use functools.cache.
    I implement it a bit inefficiently regardless, because for ease of programming,
    passing the actual substrings seemed easier to me and I recompute the value of
    the subsequences via reduce, even though this could be constant time (10*.. + ).

    I ran into some edge cases that were annoying to think about and this was fast enough.
    """

    assert len(seq) >= k

    if k == 0:
        return ()

    if len(seq) == k:
        return seq

    head, tail = seq[0], seq[1:]

    lseq = (head,) + max_k_subseq(tail, k-1)
    rseq = max_k_subseq(tail, k)

    # Inefficient path. Could be constant time in each iteration.
    lval = tuple_to_dec(lseq)
    rval = tuple_to_dec(rseq)

    return lseq if lval > rval else rseq


def main():
    puzzle_input = utils.read_example_input(
"""987654321111111
811111111111119
234234234234278
818181911112111"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input3.txt")
    puzzle_input = [list(map(int, l)) for l in puzzle_input]

    acc = 0
    for bank in puzzle_input:
        seq = max_k_subseq(tuple(bank), 12)
        acc += tuple_to_dec(seq)

    print(acc)

if __name__ == "__main__":
    main()
