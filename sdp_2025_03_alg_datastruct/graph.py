import math
import sys
from typing import Iterable

from heap_array import MinHeapArray


class Graph[T]:
    def __init__(self, nodes: Iterable[T] = None, edges: Iterable[tuple[T, T, int]] = None):
        if nodes is None:
            self.nodes = set()
        else:
            self.nodes = set(nodes)
        self.edges = dict()
        for node in self.nodes:
            self.edges[node] = {}
        if edges is not None:
            for edge in edges:
                self.add_edge(*edge)

    def add_edge(self, *edge):
        self.edges[edge[0]] [edge[1]] = edge[2]

    def __str__(self):
        result = ''
        for node in self.nodes:
            result += str(node) + ' -> '
            edge_dict = self.edges[node]
            for to, dist in edge_dict.items():
                result += f'{to}({dist}) '
            result += '\n'
        return result



    def dijkstra(self, start: T) -> tuple[dict[T, int], dict[T, T]]:
        dist: dict[T, int] = {}
        prev: dict[T, T] = {}
        pq = MinHeapArray(key = lambda node: dist[node])
        for v in self.nodes:
            dist[v] = sys.maxsize
            prev[v] = None
            pq.insert(v)
        dist[start] = 0
        while not pq.is_empty():
            u = pq.extract()
            dist_u = dist[u]
            for v, dist_u_v in self.edges[u].items():
                alt_dist = dist_u + dist_u_v
                if alt_dist < dist[v]:
                    dist[v] = alt_dist
                    pq.update_priority(v)
                    prev[v] = u
        return dist, prev


if __name__ == '__main__':
    g = Graph(chr(chcode) for chcode in range(ord('A'), ord('G')))
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'C', 8)
    g.add_edge('C', 'B', 2)
    g.add_edge('B', 'D', 3)
    g.add_edge('B', 'E', 5)
    g.add_edge('C', 'E', 5)
    g.add_edge('D', 'C', 3)
    g.add_edge('D', 'E', 1)
    g.add_edge('D', 'F', 2)
    g.add_edge('E', 'F', 1)
    print(g)
    start = 'A'
    dist, prev = g.dijkstra(start)
    for v, dist_v in dist.items():
        path = [v]
        current = v
        while current != start:
            current = prev[current]
            path.append(current)
        path.append(current)
        print(f'{v}: {dist_v}: {path.reverse()}')

