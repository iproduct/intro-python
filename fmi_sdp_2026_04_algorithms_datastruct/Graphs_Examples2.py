# 03. Даден е неориентиран граф.
# Напишете функция, която проверява дали графът е цикличен.

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cycle_rec(self, v, visited, first): # v - b -> b- c
                                            #  \ a
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.cycle_rec(i, visited, v):
                    return True
            elif i != first:
                return True
        return False

    def cycle(self):
        visited = {v: False for v in self.graph}
        for v in self.graph:
            if not visited[v]:
                if self.cycle_rec(v, visited, -1):
                    return True
        return False


graph = Graph()
graph.add_edge(1, 2) # 1-2
#                      \/
#                      3
graph.add_edge(2, 3)
graph.add_edge(3, 1)
if graph.cycle():
    print("Yes, there is a cycle.")
else:
    print("Nope.")

# 04. Даден е неориентиран граф.
# Отделно се въвеждат два върха. Намерете и изпринтирайте най-краткия път между двата върха.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, v1, vn):
        q = deque([(v1, [v1])])
        visited = set()
        while q:
            vi, path = q.popleft()

            if vi == vn:
                return path

            if vi not in visited:
                visited.add(vi)
                for i in self.graph[vi]:
                    if i not in visited:
                        q.append((i, path + [i]))
        return None


graph = Graph()
graph.add_edge(1,2) # 1 - 2 - 3 - 4 - 1
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(1,4)
v1 = 1
vn = 3
sp = graph.shortest_path(v1,vn)
if sp:
    print(*sp) #container -> *container -> for i in range(len(cont)): print(i,end="")
else:
    print("There is no path")



