import pytest
from AdjacencyListGraph import AdjacencyListGraph
from AdjacencyListDiGraph import AdjacencyListDiGraph


def test_if_creating_an_empty_adjacency_list_graph_object_results_in_adjacency_list_attribute_as_empty_dict():
    g = AdjacencyListGraph()
    assert g._adjacency_list == {}


def test_if_creating_an_empty_adjacency_list_graph_object_results_in_number_of_nodes_equals_zero():
    g = AdjacencyListGraph()
    assert g.number_of_nodes == 0


def test_if_creating_an_empty_adjacency_list_graph_object_results_in_number_of_edges_equals_zero():
    g = AdjacencyListGraph()
    assert g.number_of_edges == 0


def test_if_adding_new_node_to_adjacency_list_graph_results_in_increasing_number_of_nodes():
    g = AdjacencyListGraph()
    g.add_nodes(5, "a")
    assert g.number_of_nodes == 2


def test_if_adding_new_edge_to_adjacency_list_graph_results_in_increasing_number_of_edges():
    g = AdjacencyListGraph()
    g.add_nodes(1, 2,    3)
    g.add_edges((3, 1), (3, 2))
    assert g.number_of_edges == 2


def test_if_adding_an_existing_edge_to_adjacency_list_graph_results_in_raising_error():
    g = AdjacencyListGraph()
    g.add_nodes("a", 1)
    g.add_edges((1, "a"))
    with pytest.raises(ValueError):
        g.add_edges((1, "a"))


def test_if_adding_the_inverse_of_an_existing_edge_to_adjacency_list_graph_results_in_raising_error():
    g = AdjacencyListGraph()
    g.add_nodes("a", 1)
    g.add_edges(("a", 1))
    with pytest.raises(ValueError):
        g.add_edges((1, "a"))


def test_if_adding_existing_edge_to_adjacency_list_di_graph_results_in_raising_error():
    g = AdjacencyListDiGraph()
    g.add_nodes("a", 1)
    g.add_edges(("a", 1))
    with pytest.raises(ValueError):
        g.add_edges(("a", 1))


def test_if_adding_the_inverse_of_an_existing_edge_to_adjacency_list_di_graph_results_in_adding_new_edge():
    g = AdjacencyListDiGraph()
    g.add_nodes("a", 1)
    g.add_edges(("a", 1))
    g.add_edges((1, "a"))
    assert g._adjacency_list == {"a": {1: 1}, 1: {"a": 1}} and g.number_of_edges == 2


def test_if_adding_edge_without_weight_results_in_default_edge_weight_equals_to_one():
    g = AdjacencyListGraph()
    g.add_nodes(1, 2)
    g.add_edges((1, 2))
    v = AdjacencyListDiGraph()
    v.add_nodes("x", 4)
    v.add_edges(("x", 4))
    assert g.weight(1, 2) == 1 and v.weight("x", 4) == 1


def test_if_designation_edge_weight_results_in_recording_that_value_in_adjacency_list_structure():
    g = AdjacencyListGraph()
    g.add_nodes(1, 2)
    g.add_edges((1, 2, .3))
    v = AdjacencyListDiGraph()
    v.add_nodes("x", 4)
    v.add_edges(("x", 4, -.2))
    assert g._adjacency_list == {1: {2: .3}, 2: {1: .3}} and v._adjacency_list == {"x": {4: -.2}, 4: {}}


def test_if_neighbors_in_adjacency_list_graph_results_in_the_return_of_appropriate_vertices():
    g = AdjacencyListGraph()
    g.add_nodes(1, 2, 3)
    g.add_edges((2, 1, .3), (1, 3))
    output = []
    for vertex in g.neighbors(1):
        output.append(vertex)
    assert len(output) == 2 and set(output) == {2, 3}


def test_if_neighbors_in_adjacency_list_digraph_results_in_the_return_of_appropriate_vertices():
    g = AdjacencyListDiGraph()
    g.add_nodes(1, 2, 3)
    g.add_edges((2, 1, .3), (1, 3), (1, 2))
    output = []
    for vertex in g.neighbors(1):
        output.append(vertex)
    assert len(output) == 2 and set(output) == {2, 3}


def test_if_ingoing_neighbors_in_adjacency_list_digraph_results_in_appropriate_nodes():
    g = AdjacencyListDiGraph()
    g.add_nodes(1, 2, "a", "b")
    g.add_edges((1, 2), ("a", 2), (2, "b"))
    output = []
    for node in g.ingoing_neighbors(2):
        output.append(node)
    assert output == [1, "a"]


def test_if_ingoing_neighbors_in_adjacency_list_graph_results_in_all_neighbors():
    g = AdjacencyListGraph()
    g.add_nodes(1, 2, "a", "b")
    g.add_edges((1, 2), ("a", 2), (2, "b"))
    output = []
    for node in g.ingoing_neighbors(2):
        output.append(node)
    assert output == [1, "a", "b"]


def test_if_outgoing_neighbors_in_adjacency_list_digraph_results_in_appropriate_nodes():
    g = AdjacencyListDiGraph()
    g.add_nodes(1, 2, "a", "b")
    g.add_edges((1, 2), ("a", 2), (2, "b"))
    output = []
    for node in g.outgoing_neighbors(2):
        output.append(node)
    assert output == ["b"]


def test_if_outgoing_neighbors_in_adjacency_list_graph_results_in_all_neighbors():
    g = AdjacencyListGraph()
    g.add_nodes(1, 2, "a", "b")
    g.add_edges((1, 2), ("a", 2), (2, "b"))
    output = []
    for node in g.outgoing_neighbors(2):
        output.append(node)
    assert len(output) == 3 and set(output) == {1, "a", "b"}