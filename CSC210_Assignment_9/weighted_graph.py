# weighted_graph.py
# A weighted graph stored using an adjacency list
# Modified by: Nathan Huffman
# Note: Please write this yourself, not using an LLM.
from queue import PriorityQueue
from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class WeightedEdge:
    weight: float | int
    from_: str
    to: str 


class WeightedGraph:

    def __init__(self):
        self._adjacency_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = set()
            
    def add_edge(self, from_, to, weight, bidirectional=True):
        if from_ not in self._adjacency_list:
            self._adjacency_list[from_] = set()
        self._adjacency_list[from_].add(WeightedEdge(weight, from_, to))
        if bidirectional:
            if to not in self._adjacency_list:
                self._adjacency_list[to] = set()
            self._adjacency_list[to].add(WeightedEdge(weight, to, from_))
        else:
            if to not in self._adjacency_list:
                self.add_vertex(to)
                
    def neighbors(self, vertex):
        assert vertex in self._adjacency_list, "Vertex not in graph"
        return {edge.to for edge in self._adjacency_list[vertex]}
    
    def edges_from(self, vertex):
        assert vertex in self._adjacency_list, "Vertex not in graph"
        return self._adjacency_list[vertex]
    
    def edge_exists(self, from_, to):
        if from_ not in self._adjacency_list:
            return False
        return to in self.neighbors(from_)
    
    def path_map_to_path(self, previous_map, goal):
        path = []
        current = goal
        while True:
            path.insert(0, current)
            previous = previous_map[current]
            if previous == current:
                break
            current = previous
        return path

    # Perform dijkstra's algorithm from *start*, looking through
    # the entire graph
    # Returns a pair containing the *parents* (how to get to each vertex)
    # and the *distances* (how far each vertex is from the start) tables
    def dijkstra(self, start):
        # Parents and distances are tracked as dictionaries from start.
        parents = {start: start}
        distances = {start: 0}
        
        # Create frontier and add start to priority queue.
        frontier = PriorityQueue()
        frontier.put((0, start))

        # Empty frontier, starting with the current vertex and distance.  
        while not frontier.empty():
            (current_distance, current) = frontier.get()
            # For each edge of current, find total distance if edge travelled.
            for edge in self._adjacency_list[current]:
                new_distance = current_distance + edge.weight
                # If new path shorter, or edge distance hasn't been tracked...
                if edge.to not in distances or new_distance < distances[edge.to]:
                    # Record distances + parents; add new distance to frontier.
                    distances[edge.to] = new_distance
                    parents[edge.to] = current
                    frontier.put((new_distance, edge.to))
        # Return parents and distances as tuple.
        return parents, distances
    
    
    def __str__(self):
        return '\n'.join(f"{vertex}: {[f'{edge.to}({edge.weight})' for edge in edges]}"
                         for vertex, edges in self._adjacency_list.items())