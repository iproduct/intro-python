NodeType = type(str)

class Graph:
    def __init__(self, nodes: list[NodeType] = None, edges: list[tuple[NodeType, NodeType, int]] = None) -> None:
        self.nodes: set[NodeType] = set() if nodes is None else set(nodes)
        self.edges: dict[NodeType, dict[NodeType, int]] = dict()
        for node in nodes:
            self.edges[node]: dict[NodeType, int] = dict()
        if edges is not None:
            for edge in edges:
                self.add_edge(*edge)

    def __str__(self):
        result = ''
        nodes_sorted = list(self.nodes)
        nodes_sorted.sort()
        for node in nodes_sorted:
            result += f'{node} -> {self.edges[node]}\n'
        return result


    def add_edge(self, start: NodeType, end: NodeType, dist: int) -> None:
        self.edges[start][end] = dist

    def dijkstra(self, initial: NodeType) -> tuple[dict[NodeType, int], dict[NodeType, NodeType]]:
        visited: dict[NodeType, int] = {initial: 0}
        prev: dict[NodeType, NodeType] = {}

        nodes = set(self.nodes)

        while nodes:
            min_node = None
            #find min node
            for node in nodes: # O(n) -> need to improve
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            # process min node
            nodes.remove(min_node)
            concurrent_weight = visited[min_node]

            for edge_node in self.edges[min_node]:
                edge_weight = self.edges[min_node][edge_node]
                if edge_node not in visited or concurrent_weight + edge_weight < visited[edge_node]:
                    visited[edge_node] = concurrent_weight + edge_weight
                    prev[edge_node] = min_node

        return visited, prev

if __name__ == '__main__':
    g = Graph([chr(chcode) for chcode in range(ord('A'),ord('G'))])
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
    print(dist)
    print(prev)

    for node in dist:
        path = []
        nxt = node
        while nxt != start:
            path.append(nxt)
            nxt = prev[nxt]
        path.append(start)
        path.reverse()
        print(f'{node}: {dist[node]} -> {path}')