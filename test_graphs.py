import pytest

from graphs import AdjacencyListGraph, Graph  #  AdjacencyListDiGraph, AdjacencyMatrixGraph, AdjacencyMatrixDiGraph


def test_if_adjacency_list_instance_is_an_instance_of_graph_specification_abc_class():
    assert isinstance(AdjacencyListGraph(), Graph) is True


def test_if_adding_duplicated_nodes_results_in_raising_exception():
    g = AdjacencyListGraph()
    with pytest.raises(ValueError):
        g.add_node(2, 2)


def test_if_creating_adjacency_list_instance_results_in_number_of_nodes_equals_to_zero():
    g = AdjacencyListGraph()
    assert g.number_of_nodes == 0


def test_if_adding_new_nodes_will_increase_the_number_of_nodes():
    g = AdjacencyListGraph()
    g.add_node(2, "xy")
    assert g.number_of_nodes == 2


def test_if_adding_new_edge_including_node_that_not_exists_results_in_raising_value_error():
    g = AdjacencyListGraph()
    g.add_node(2, "xy")
    with pytest.raises(ValueError):
        g.add_edge((1, 2))


def test_if_adding_edge_without_weight_results_in_default_weight_value_equals_to_one():
    g = AdjacencyListGraph()
    g.add_node(1, "xy")
    g.add_edge((1, "xy"))
    assert g.container[1]["xy"]["weight"] == 1
