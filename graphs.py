import abc


class Graph(abc.ABC):
    def __init__(self):
        self._container = {}
        self._number_of_nodes = 0
        self._number_of_edges = 0

    @property
    def container(self):
        return self._container

    @property
    def number_of_nodes(self):
        return len(self._container)

    @property
    def number_of_edges(self):
        return self._number_of_edges

    def add_node(self, *args) -> None:
        for node in args:
            if node in self._container.keys():
                raise ValueError
            self._container[node] = self._container.get(node, {})

    @abc.abstractmethod
    def add_edge(self, *args: tuple) -> None:
        pass

    def nodes(self):  # generator that provides iterating over vertices
        nodes_iterator = iter(self._container.keys())
        try:
            while True:
                next_node = next(nodes_iterator)
                yield next_node
        except StopIteration:
            pass

    @abc.abstractmethod
    def outgoing_neighbors(self, node):
        pass

    @abc.abstractmethod
    def ingoing_neighbors(self, node):
        pass

    @abc.abstractmethod
    def neighbors(self, node):
        pass


class AdjacencyListGraph(Graph):
    def ingoing_neighbors(self, node):
        pass

    def outgoing_neighbors(self, node):
        pass

    def neighbors(self, node):
        pass

    def add_edge(self, *args):
        for edge in args:
            if len(edge) > 3 or len(edge) < 2 or edge[0] not in self._container.keys() or \
                    edge[1] not in self._container.keys():
                raise ValueError
            u, v = edge[0], edge[1]
            if len(edge) == 3:
                weight = edge[2]
            else:
                weight = 1
            self._container[u][v] = self._container[u].get(v, {"weight": weight})
            self._container[v][u] = self._container[v].get(u, {"weight": weight})


# class AdjacencyListDiGraph(Graph):
#     def add_edge(self, edge):
#         pass
#
#
# class AdjacencyMatrixDiGraph(Graph):
#     def add_edge(self, edge):
#         pass
#
#

class AdjacencyMatrixGraph(Graph):
    def neighbors(self, node):
        pass

    def ingoing_neighbors(self, node):
        pass

    def outgoing_neighbors(self, node):
        pass

    def add_edge(self, *args):
        pass


if __name__ == '__main__':
    g = AdjacencyListGraph()
    g.add_node("A", "B", "C")
    g.add_edge(("A", "B"))
    print(g.container)
    print(g.container["A"]["B"]["weight"])
    # adjacency_matrix_graph = AdjacencyMatrixGraph()
    # print(adjacency_matrix_graph.container)
