import numpy as np

E = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('B', 'E'), ('F', 'E')]
V_set = set()
for edge in E:
    V_set.add(edge[0])
    V_set.add(edge[1])
V = list(V_set)
V.sort()
print(V)

def get_adj_matrix(V, E):
    matrix = np.zeros((len(V), len(V)), dtype=int)
    V_index_map = {v: i for i, v in enumerate(V)}
    for edge in E:
        matrix[V_index_map[edge[0]], V_index_map[edge[1]]] = 1
    return matrix

def vert_out_degrees(V, E):
    am = get_adj_matrix(V, E)
    degrees = [int(sum(row)) for row in am]
    return degrees

print(get_adj_matrix(V, E))
print(vert_out_degrees(V, E))
