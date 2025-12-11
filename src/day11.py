from collections import deque
from pprint import pprint

import graphviz

import utils


def count_paths(start: str, target: str, stop_at: set[str], graph: dict[str, list[str]]) -> int:
    """Count the number of paths from start to a target.

    The `stop_at` set is an optional optimization to let the algorithm know beyond
    which nodes the target cannot be anymore because of the structure of the graph.
    """

    path_count = 0
    Q = deque([start])
    while Q:
        node = Q.popleft()

        if node == target:
            path_count += 1
            continue

        if node in stop_at:
            continue

        Q.extend(graph.get(node, []))

    return path_count


def render_graph(graph: dict[str, list[str]]):
    dot = graphviz.Digraph()
    for n in graph.keys():
        dot.node(n)

    for n, adj in graph.items():
        for a in adj:
            dot.edge(n, a)

    dot.render("inputs/input10_graph.gv")


def main():
    puzzle_input = utils.read_example_input(
        """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    )
    puzzle_input = utils.read_puzzle_input("inputs/input11.txt")

    graph = {}
    for line in puzzle_input:
        node, *neighbors = line.replace(":", "").split()
        graph[node] = neighbors

    # Part1: Count paths from you -> out directly.
    part1_count = count_paths(start="you", target="out", stop_at=set(), graph=graph)
    print(part1_count)

    # Part2: Count paths by partitioning the graph manually

    # We inspect the graph visually, as is sometimes the trick in advent of code.
    render_graph(graph)

    # We have seen that the graph has a few "bottleneck" nodes, which we use both
    # as a partitioning point (i.e. wfq later) and to stop the exploration of the path.
    part2_svr_fft = count_paths(start="svr", target="fft", stop_at={"mig", "mef", "jqs", "omk"}, graph=graph)

    # From fft to dac is quite far. The visualization showed that any path to dac will
    # go through the bottlenecks wfq, oqq and acf, with dac then just some steps beyond these.
    part2_fft_wfq = count_paths(start="fft", target="wfq", stop_at={"jsh", "oqq", "htf", "acf"}, graph=graph)
    part2_fft_oqq = count_paths(start="fft", target="oqq", stop_at={"jsh", "wfq", "htf", "acf"}, graph=graph)
    part2_fft_acf = count_paths(start="fft", target="acf", stop_at={"jsh", "wfq", "htf", "oqq"}, graph=graph)

    part2_wfq_dac = count_paths(start="wfq", target="dac", stop_at={"you", "dwp", "bxs"}, graph=graph)
    part2_oqq_dac = count_paths(start="oqq", target="dac", stop_at={"you", "dwp", "bxs"}, graph=graph)
    part2_acf_dac = count_paths(start="acf", target="dac", stop_at={"you", "dwp", "bxs"}, graph=graph)

    # The final stretch is a smaller subgraph again.
    part2_dac_out = count_paths(start="dac", target="out", stop_at=set(), graph=graph)

    # Now we mulitply the independent path segments and add them up.
    part2_total = (
        part2_svr_fft * part2_fft_wfq * part2_wfq_dac * part2_dac_out
        + part2_svr_fft * part2_fft_oqq * part2_oqq_dac * part2_dac_out
        + part2_svr_fft * part2_fft_acf * part2_acf_dac * part2_dac_out
    )

    print(part2_total)


if __name__ == "__main__":
    main()
