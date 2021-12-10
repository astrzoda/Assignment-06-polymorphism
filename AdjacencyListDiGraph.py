from Graph import Graph
import logging
from typing import Generic, TypeVar


Node = TypeVar("Node")
T = TypeVar("T")


class AdjacencyListDiGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self._adjacency_list = {}

    @property
    def number_of_nodes(self) -> int:
        return len(self._adjacency_list)

    def weight(self, source, destination) -> float:
        if destination not in self._adjacency_list[source].keys():
            raise ValueError
        return self._adjacency_list[source][destination]

    # validation of adding nodes
    def add_nodes(self, *nodes) -> None:
        unique_input_nodes = set(nodes)
        if len(unique_input_nodes) < len(nodes) or any(element in unique_input_nodes for element in
                                                       self._adjacency_list.keys()):
            raise ValueError()
            # logging.basicConfig()
            # logger = logging.getLogger(__name__)
            # logger.warning("Duplicated nodes")
        for node in nodes:
            self._adjacency_list[node] = {}

    def nodes(self):
        return self._adjacency_list.keys()

    def add_edges(self, *edges: tuple) -> None:
        for edge in edges:
            if len(edge) > 3 or len(edge) < 2 or edge[0] not in self._adjacency_list.keys() or \
                    edge[1] not in self._adjacency_list.keys():
                raise ValueError
            source, destination = edge[0], edge[1]
            if destination in self._adjacency_list[source].keys():  # raise error if edge already exists
                raise ValueError
            if len(edge) == 3:
                if edge[2] == 0:
                    raise ValueError
                weight = edge[2]
            else:
                weight = 1
            self._adjacency_list[source][destination] = weight
            self._number_of_edges += 1

    def edges(self):
        for vertex, neighborhood in self._adjacency_list.items():
            for neighbor in neighborhood:
                yield vertex, neighbor

    def neighbors(self, node):
        for vertex, neighborhood in self._adjacency_list.items():
            if vertex == node:
                for neighbor in self._adjacency_list[vertex]:
                    yield neighbor
            else:
                if vertex not in self._adjacency_list[node].keys() and node in self._adjacency_list[vertex]:
                    yield vertex

    def ingoing_neighbors(self, node):
        for vertex, neighborhood in self._adjacency_list.items():
            if vertex != node:
                if node in neighborhood:
                    yield vertex

    def outgoing_neighbors(self, node):
        return self._adjacency_list[node].keys()
