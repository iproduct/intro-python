NodeType = type(str)

class Graph:
    def __init__(self, nodes: list(NodeType) = None, edges: list[tuple[NodeType, NodeType, int]] = None) -> None:
        self.nodes: set[NodeType] = set() if nodes is None else set(nodes)
        self.edges: dict[NodeType, dict[NodeType, int]] = dict()
        for node in nodes:
            self.edges[node]: dict[NodeType, int] = dict()
        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def add_edge(self, edge: tuple[NodeType, NodeType, int]) -> None:
        self.edges[edge[0]][edge[1]] = edge[2]

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