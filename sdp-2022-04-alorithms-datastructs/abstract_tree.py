from typing import Callable


class AbstractTree:
    def size(self):
        raise NotImplemented('Method not implemented.')
    def values_dfs_preorder(self):
        raise NotImplemented('Method not implemented.')
    def values_dfs_postorder(self):
        raise NotImplemented('Method not implemented.')
    def nodes_dfs_preorder(self):
        raise NotImplemented('Method not implemented.')
    def nodes_dfs_postrder(self):
        raise NotImplemented('Method not implemented.')
    def nodes_bfs_preorder(self):
        raise NotImplemented('Method not implemented.')
    def root(self):
        raise NotImplemented('Method not implemented.')
    def parent(self, p):
        raise NotImplemented('Method not implemented.')
    def children(self, p):
        raise NotImplemented('Method not implemented.')
    def is_empty(self):
        raise NotImplemented('Method not implemented.')
    def is_internal(self, node):
        raise NotImplemented('Method not implemented.')
    def is_root(self, node):
        raise NotImplemented('Method not implemented.')
    def swap_elements(self, p, q):
        raise NotImplemented('Method not implemented.')
    def replace_element(self, p, o):
        raise NotImplemented('Method not implemented.')
    def find(self, value):
        raise NotImplemented('Method not implemented.')
    def find_first(self, value):
        raise NotImplemented('Method not implemented.')
    def find_by_predicate(self, predicate, start_from = None):
        raise NotImplemented('Method not implemented.')

