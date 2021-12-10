import pytest
from Dijkstra import Dijkstra
from AdjacencyListDiGraph import AdjacencyListDiGraph
from Dijkstra_oop import Dijkstra

G = AdjacencyListDiGraph()
G.add_nodes("A", "B", "C", "D", "E")
G.add_edges(("A", "B", 2), ("A", "D", 4), ("B", "C", 3), ("B", "D", 3), ("C", "E", 2), ("D", "E", 4), ("D", "C", 3))


def test_if_shortest_path_result_in_appropriate_sequence_of_vertices():
    dijkstra = Dijkstra()
    assert dijkstra.shortest_path(G, "A", "E") == ["A", "B", "C", "E"]

