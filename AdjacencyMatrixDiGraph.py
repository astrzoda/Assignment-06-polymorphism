from Graph import Graph


class AdjacencyMatrixDiGraph(Graph):
    def __init__(self):
        super().__init__()
        self._adjacency_matrix = []
        self._nodes_labels = []

    def nodes(self):
        nodes_iterator = iter(self._nodes_labels)
        try:
            while True:
                next_node = next(nodes_iterator)
                yield next_node
        except StopIteration:
            pass

    def weight(self, source, destination):
        source_index_label = self._nodes_labels.index(source)
        destination_index_label = self._nodes_labels.index(destination)
        if self._adjacency_matrix[source_index_label][destination_index_label] == 0:
            raise ValueError
        else:
            return self._adjacency_matrix[source_index_label][destination_index_label]

    def add_edges(self, *edges: tuple) -> None:
        for edge in edges:
            if len(edge) > 3 or len(edge) < 2 or edge[0] not in self._nodes_labels or \
                    edge[1] not in self._nodes_labels:
                raise ValueError
            source, destination = edge[0], edge[1]
            source_label_index, destination_label_index = self._nodes_labels.index(source),\
                                                          self._nodes_labels.index(destination)
            if self._adjacency_matrix[source_label_index][destination_label_index] != 0:
                raise ValueError
            if len(edge) == 3:
                if edge[2] == 0:
                    raise ValueError
                weight = edge[2]
            else:
                weight = 1
            self._adjacency_matrix[source_label_index][destination_label_index] = weight
            self._number_of_edges += 1

    def edges(self):
        for i in range(self.number_of_nodes):
            j = 0
            for k in range(j, self.number_of_nodes):
                if self._adjacency_matrix[i][k] != 0:
                    yield self._nodes_labels[i], self._nodes_labels[k]
                j += 1

    def neighbors(self, node):
        node_index = self._nodes_labels.index(node)
        for i in range(self._number_of_nodes):
            if self._adjacency_matrix[i][node_index] != 0 or self._adjacency_matrix[node_index][i] != 0:
                yield self._nodes_labels[i]

    def ingoing_neighbors(self, node):
        node_index = self._nodes_labels.index(node)
        for j, row in enumerate(self._adjacency_matrix):
            print("row", row)
            if row[node_index] != 0:
                neighbor_index = j
                yield self._nodes_labels[neighbor_index]

    def outgoing_neighbors(self, node):
        node_index = self._nodes_labels.index(node)
        neighbors_iterator = iter(self._adjacency_matrix[node_index])
        neighbors_index = 0
        try:
            while True:
                neighbor = next(neighbors_iterator)
                if neighbor != 0:
                    yield self._nodes_labels[neighbors_index]
                neighbors_index += 1
        except StopIteration:
            pass

    def add_nodes(self, *nodes):
        for node in nodes:
            if node in self._nodes_labels:
                raise ValueError
            self._nodes_labels.append(node)
            self._adjacency_matrix.append([0]*self.number_of_nodes)
            for row in self._adjacency_matrix:
                row.append(0)
            self._number_of_nodes += 1
