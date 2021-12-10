from AdjacencyMatrixDiGraph import AdjacencyMatrixDiGraph
from AdjacencyMatrixGraph import AdjacencyMatrixGraph
from AdjacencyListDiGraph import AdjacencyListDiGraph
from AdjacencyListGraph import AdjacencyListGraph

if __name__ == '__main__':
    # my_graph = AdjacencyMatrixDiGraph()
    # my_graph.add_node("x", 55, 1)
    # my_graph.add_edge(("x", 1), (1, "x"))
    # for edge in my_graph.edges():
    #     print(edge)
    my_graph = AdjacencyListGraph()
    my_graph.add_nodes(3, "x")
    my_graph.add_nodes(2)
    # print(my_graph.number_of_nodes)
    # def naive_zip(first: Sequence[Any], second: Sequence[Any]) -> Iterable[tuple[Any, Any]]:
    for v in my_graph.nodes():
        pass
    # print(my_graph.nodes)

