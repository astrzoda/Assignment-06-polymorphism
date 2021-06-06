import math


class Dijkstra:
    def __init__(self):
        self.distances = {}
        self.previous_vertices = {}
        self.visited = []

    def shortest_path(self, graph, source, destination):
        self.init_attribute_values(graph, source)
        current_node = source
        while len(self.visited) != graph.number_of_nodes:
            for neighbor in graph.outgoing_neighbors(current_node):
                current_edge_weight = graph.weight(current_node, neighbor)
                if current_edge_weight < 0:
                    raise ValueError
                total_cost_from_source = self.distances[current_node] + current_edge_weight
                if total_cost_from_source < self.distances[neighbor]:
                    self.distances[neighbor] = total_cost_from_source
                    self.previous_vertices[neighbor] = current_node
            self.visited.append(current_node)
            unvisited_dv = {key: value for key, value in self.distances.items() if key not in self.visited}
            if unvisited_dv != {}:
                current_node = min(unvisited_dv, key=unvisited_dv.get)
        return self.read_path(source, destination)

    def init_attribute_values(self, graph, source):
        self.distances[source] = 0
        for node in graph.nodes():
            self.distances[node] = self.distances.get(node, math.inf)

    def read_path(self, source, destination):
        previous_node = destination
        path = [destination]
        while previous_node != source:
            previous_node = self.previous_vertices[previous_node]
            path.append(previous_node)
        return path[::-1]

    def shortest_paths(self, graph, source):
        for node in graph.nodes():
            destination = node
            return self.shortest_path(graph, source, destination)


