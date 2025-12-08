import math

import numpy as np
from scipy.cluster.hierarchy import DisjointSet
from scipy.spatial.distance import pdist, squareform

import utils


def main():
    puzzle_input = utils.read_example_input(
"""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input8.txt")

    arr = np.array([list(map(int, line.split(","))) for line in puzzle_input])
    n = len(arr)

    # Crazy pairwise distance stuff
    dists = pdist(arr)
    dists = squareform(dists)

    # Don't want to consider self-connections or symmetrical ones.
    dists[np.tril_indices(dists.shape[0], k=0)] = np.inf

    clusters = DisjointSet(range(n))

    limit = 1000 if True else 10000000000 # Toggle part 1 and 2!
    for idx in np.argsort(dists, axis=None)[:limit]:
        n1, n2 = np.unravel_index(idx, dists.shape)
        clusters.merge(n1, n2)

        if len(clusters.subsets()) == 1:
            c1, c2 = arr[n1], arr[n2]
            print(f"Connected all at {c1}, {c2}: {c1[0]*c2[0]}")
            return
    
    # If we didn't return early due to part 2, print solution to part 1 here.
    cluster_count = [len(s) for s in clusters.subsets()]
    max_clusters = sorted(cluster_count)[-3:]
    print(math.prod(max_clusters))


if __name__ == "__main__":
    main()
