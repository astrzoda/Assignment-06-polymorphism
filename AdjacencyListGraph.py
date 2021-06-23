from AdjacencyListDiGraph import AdjacencyListDiGraph


class AdjacencyListGraph(AdjacencyListDiGraph):
    def add_edges(self, *edges: tuple) -> None:
        super().add_edges(*edges)
        for pair in edges:
            source, destination = pair[0], pair[1]
            weight = self._adjacency_list[source][destination]
            self._adjacency_list[destination][source] = weight

    def edges(self):
        checked_vertices = []
        for vertex, neighborhood in self._adjacency_list.items():
            checked_vertices.append(vertex)
            for neighbor in neighborhood:
                if neighbor not in checked_vertices:
                    yield vertex, neighbor
