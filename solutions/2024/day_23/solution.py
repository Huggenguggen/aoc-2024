# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/23

from ...base import StrSplitSolution, answer
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt

class Solution(StrSplitSolution):
    _year = 2024
    _day = 23

    @answer(1302)
    def part_1(self) -> int:
        self.graph = nx.Graph()
        historian_nodes = set()
        all_nodes = set()

        for l in self.input:
            node1, node2 = l.rstrip().split("-")
            self.graph.add_node(node1)
            self.graph.add_node(node2)
            self.graph.add_edge(node1, node2)
            if node1.startswith("t"):
                historian_nodes.add(node1)
            if node2.startswith("t"):
                historian_nodes.add(node2)
            all_nodes.add(node1)
            all_nodes.add(node2)

        total = set()
        for h in historian_nodes:
            n = list(self.graph.neighbors(h))
            for f, t in combinations(n, 2):
                if self.graph.has_edge(f, t):
                    l = [h, f, t]
                    l.sort()
                    total.add(tuple(l))
        
        return len(total)

    @answer("cb,df,fo,ho,kk,nw,ox,pq,rt,sf,tq,wi,xz")
    def part_2(self) -> int:
        print(self.graph)
        cliques = nx.find_cliques(self.graph)
        clique = None
        for c in cliques:
            if not clique:
                clique = c 
            clique = c if len(c) > len(clique) else clique            
        clique = list(clique)
        clique.sort()
        return ",".join(clique)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
