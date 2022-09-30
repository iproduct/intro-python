NodeType = type(str)
class Graph:
    def __init__(self):
        self.nodes: set[NodeType] = set()
        self.edges: dict[NodeType, set[NodeType]] = {}
        self.distances: dict[tuple[NodeType, NodeType], int] = {}

    def add_node(self, node: NodeType):
        self.nodes.add(node)
        self.edges[node] = set()

    def add_edge(self, from_node: NodeType, to_node: NodeType, distance: int):
        self.edges[from_node].add(to_node)
        # self.edges[to_node].add(from_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph: Graph, initial: NodeType):
    visited: dict[NodeType, int] = {initial: 0}
    prev: dict[NodeType, NodeType] = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None # infinity
        # find min_node
        for node in nodes: # O(N) to improve
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        # process min_node
        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge_node in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge_node)]
            if edge_node not in visited or weight < visited[edge_node]:
                visited[edge_node] = weight
                prev[edge_node] = min_node

    return visited, prev

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_node(chr(ord('A') + i))
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

    start = 'A'
    distances, prev = dijkstra(g, start)
    for node, min_distance in distances.items():
        print(f'To node: {node} = {min_distance}: ', end='')
        path  = []
        current_node = node
        while current_node != start:
            path.append(current_node)
            current_node = prev[current_node]
        path.append(start)
        path.reverse()
        print(path)