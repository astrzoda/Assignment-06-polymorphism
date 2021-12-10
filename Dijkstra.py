import math
from AdjacencyListDiGraph import AdjacencyListDiGraph


def shortest_path(graph, source, destination):
    previous_vertices, distances, visited_vertices = {}, {source: 0}, []
    for node in graph.nodes():
        distances[node] = distances.get(node, math.inf)

    current_node = source
    while len(visited_vertices) != graph.number_of_nodes:
        for neighbor in graph.outgoing_neighbors(current_node):
            current_edge_weight = graph.weight(current_node, neighbor)
            if current_edge_weight < 0:
                raise ValueError
            total_cost_from_source = distances[current_node] + current_edge_weight
            if total_cost_from_source < distances[neighbor]:
                distances[neighbor] = total_cost_from_source
                previous_vertices[neighbor] = current_node
        visited_vertices.append(current_node)
        unvisited_dv = {key: value for key, value in distances.items() if key not in visited_vertices}
        if len(unvisited_dv) != 0:
            current_node = min(unvisited_dv, key=unvisited_dv.get)
    return read_path(source, destination, previous_vertices)


def read_path(source, destination, previous_vertices):
    previous_node = destination
    path = [destination]
    while previous_node != source:
        previous_node = previous_vertices[previous_node]
        path.append(previous_node)
    return path[::-1]


if __name__ == '__main__':
    G = AdjacencyListDiGraph()
    G.add_nodes("A", "B", "C", "D", "E")
    G.add_edges(("A", "B", 2), ("A", "D", 4), ("B", "C", 3), ("B", "D", 3), ("C", "E", 2), ("D", "E", 4), ("D", "C", 3))
    test1 = shortest_path(G, "A", "E") == ["A", "B", "C", "E"]
    print(test1)