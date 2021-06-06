from AdjacencyMatrixDiGraph import AdjacencyMatrixDiGraph


class AdjacencyMatrixGraph(AdjacencyMatrixDiGraph):
    def __init__(self):
        super().__init__()

    def add_edge(self, *args: tuple) -> None:
        super().add_edge(*args)
        for edge in args:
            source, destination = edge[0], edge[1]
            source_label_index, destination_label_index = self._nodes_labels.index(source),\
                                                          self._nodes_labels.index(destination)
            self._adjacency_matrix[destination_label_index][source_label_index] = \
                self._adjacency_matrix[source_label_index][destination_label_index]

    def edges(self):
        for i in range(self.number_of_nodes):
            j = 0
            for k in range(j+i, self.number_of_nodes):
                if self._adjacency_matrix[i][k] != 0:
                    yield self._nodes_labels[i], self._nodes_labels[k]
                j += 1

