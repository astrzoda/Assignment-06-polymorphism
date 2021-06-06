# from typing import Protocol
import abc


class Graph(abc.ABC):
    def __init__(self):
        self._number_of_nodes = 0
        self._number_of_edges = 0

    @property
    def number_of_nodes(self):
        return self._number_of_nodes

    @property
    def number_of_edges(self):
        return self._number_of_edges

    @abc.abstractmethod
    def weight(self, source, destination):
        pass

    @abc.abstractmethod
    def add_node(self, node):
        pass

    @abc.abstractmethod
    def nodes(self):
        pass

    @abc.abstractmethod
    def add_edge(self, *args: tuple) -> None:
        pass

    @abc.abstractmethod
    def edges(self):
        pass

    @abc.abstractmethod
    def neighbors(self, node):
        pass

    @abc.abstractmethod
    def ingoing_neighbors(self, node):
        pass

    @abc.abstractmethod
    def outgoing_neighbors(self, node):
        pass
