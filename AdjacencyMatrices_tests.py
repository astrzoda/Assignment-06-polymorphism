import pytest
from AdjacencyMatrixGraph import AdjacencyMatrixGraph
from AdjacencyMatrixDiGraph import AdjacencyMatrixDiGraph


def test_if_adding_duplicated_nodes_results_in_raising_error():
    g = AdjacencyMatrixGraph()
    with pytest.raises(ValueError):
        g.add_nodes(2, 2)


def test_if_adding_an_existing_node_to_adjacency_matrix_graph_results_in_raising_error():
    g = AdjacencyMatrixGraph()
    g.add_nodes(1)
    with pytest.raises(ValueError):
        g.add_nodes(1)


def test_if_adding_edge_with_weight_equals_to_zero_results_in_raising_error():
    g = AdjacencyMatrixGraph()
    g.add_nodes(2, "x")
    with pytest.raises(ValueError):
        g.add_edge((2, "x", 0))


# def test_if_adding_edge_with_weight_that_is_no_numeric_value_results_in_raising_error():
#     g = AdjacencyMatrixGraph()
#     g.add_node(2, "x")
#     with pytest.raises(ValueError):
#         g.add_edge((2, "x"))


def test_if_creating_adjacency_matrix_graph_instance_results_in_number_of_nodes_equals_to_zero():
    g = AdjacencyMatrixGraph()
    assert g.number_of_nodes == 0


def test_if_adding_new_nodes_will_increase_the_number_of_nodes():
    g = AdjacencyMatrixGraph()
    g.add_nodes(2, "x")
    assert g.number_of_nodes == 2


def test_if_adding_nodes_to_an_empty_adjacency_matrix_graph_results_in_squared_matrix_filled_with_zeros():
    g = AdjacencyMatrixGraph()
    g.add_nodes(2, "x", 6)
    assert g._adjacency_matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_if_adding_new_edge_including_node_that_not_exists_in_adjacency_matrix_results_in_raising_value_error():
    g = AdjacencyMatrixGraph()
    g.add_nodes(2, "xy")
    with pytest.raises(ValueError):
        g.add_edges(("john doe", 2))


def test_if_adding_edge_without_weight_to_adjacency_matrix_graph_results_in_default_weight_value_equals_to_one():
    g = AdjacencyMatrixGraph()
    g.add_nodes(1, "xy")
    g.add_edges((1, "xy"))
    assert g.weight("xy", 1) == 1


def test_if_adding_edges_with_weights_to_adjacency_matrix_graph_results_in_symmetrical_matrix_with_appropriate_coefficients():
    g = AdjacencyMatrixGraph()
    g.add_nodes("a", "b", 1)
    g.add_edges(("a", "b"), ("a", 1, .5))
    assert g._adjacency_matrix == [[0, 1, .5], [1, 0, 0], [.5, 0, 0]]


def test_if_adding_edges_with_weights_to_adjacency_matrix_digraph_results_in_matrix_with_appropriate_coefficients():
    g = AdjacencyMatrixDiGraph()
    g.add_node("a", "b", 1)
    g.add_edge(("a", "b"), ("a", 1, .5))
    assert g._adjacency_matrix == [[0, 1, .5], [0, 0, 0], [0, 0, 0]]


def test_if_adding_the_inverse_of_an_existing_edge_to_adjacency_matrix_di_graph_results_in_adding_new_edge():
    g = AdjacencyMatrixDiGraph()
    g.add_node(1, 2)
    g.add_edge((1, 2))
    g.add_edge((2, 1))
    assert g._adjacency_matrix == [[0, 1], [1, 0]] and g.number_of_edges == 2


def test_if_adding_the_inverse_of_an_existing_edge_to_adjacency_matrix_graph_results_in_raise_error():
    g = AdjacencyMatrixGraph()
    g.add_node(1, 2)
    g.add_edge((1, 2))
    with pytest.raises(ValueError):
        g.add_edge((2, 1))


def test_if_adding_the_existing_edge_to_adjacency_matrix_graph_results_in_raise_error():
    g = AdjacencyMatrixGraph()
    g.add_node(1, 2)
    g.add_edge((1, 2))
    with pytest.raises(ValueError):
        g.add_edge((1, 2))


def test_if_outgoing_neighbors_function_in_adjacency_matrix_digraph_results_in_appropriate_nodes():
    g = AdjacencyMatrixDiGraph()
    g.add_node("a", "b", 1)
    g.add_edge(("a", "b"), ("a", 1, .5), ("b", "a"))
    output = []
    for vertex in g.outgoing_neighbors("a"):
        output.append(vertex)
    assert set(output) == {"b", 1}


def test_if_ingoing_neighbors_function_in_adjacency_matrix_digraph_results_in_appropriate_nodes():
    g = AdjacencyMatrixDiGraph()
    g.add_node("a", "b", 1)
    g.add_edge(("a", "b"), ("a", 1, .5))
    output = []
    for vertex in g.ingoing_neighbors(1):
        output.append(vertex)
    assert output == ["a"]


def test_if_neighbors_function_in_adjacency_matrix_digraph_results_in_appropriate_nodes():
    g = AdjacencyMatrixDiGraph()
    g.add_node("a", "b", 1)
    g.add_edge(("a", "b"), ("a", 1, .5))
    output = []
    for vertex in g.neighbors("a"):
        output.append(vertex)
    assert output == ["b", 1]


def test_if_iterating_over_edges_in_adjacency_matrix_digraph_results_in_appropriate_tuples():
    g = AdjacencyMatrixDiGraph()
    g.add_node("a", "b", 1)
    g.add_edge(("a", "b"), ("a", 1, .5))
    output = []
    for edge in g.edges():
        output.append(edge)
    assert output == [("a", "b"), ("a", 1)]