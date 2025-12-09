# graph.py
# A graph stored using an adjacency list
# Modified by: Nathan Huffman
# Note: Please write this yourself, not using an LLM.
from stack import Stack
from que import Queue


class Graph:
    def __init__(self):
        self._adjacency_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = set()
            
    def add_edge(self, from_, to, bidirectional=True):
        if from_ not in self._adjacency_list:
            self._adjacency_list[from_] = set()
        self._adjacency_list[from_].add(to)
        if bidirectional:
            if to not in self._adjacency_list:
                self._adjacency_list[to] = set()
            self._adjacency_list[to].add(from_)
        else:
            if to not in self._adjacency_list:
                self.add_vertex(to)
                
    def neighbors(self, vertex):
        assert vertex in self._adjacency_list, "Vertex not in graph"
        return self._adjacency_list[vertex]
    
    # Return whether or not *from_* exists in the graph,
    # and  *to* is one of its neighbors
    # Return True only if both criteria are true
    def edge_exists(self, from_, to):
        return (from_ in self._adjacency_list and to in self.neighbors(from_)) 

    
    # Work backwards to find a path from your dfs()
    # or bfs() goal using the explored dictionary as
    # the previous_map
    def _path_map_to_path(self, previous_map, goal):
        path = []
        current = goal
        while True:
            path.insert(0, current)
            previous = previous_map[current]
            if previous == current:
                break
            current = previous
        return path
    
    def dfs(self, start, goal):
        # Explored keeps track of where we've been and how we got there.
        explored = {}
        explored[start] = start
        
        # The frontier is created with a stack and the start is pushed to it.
        frontier = Stack()
        frontier.push(start)

        # Loop while the frontier is not empty and pop current of the frontier.
        while not frontier.is_empty:
            current = frontier.pop()

            # Check if current is the goal and if so, return the path.
            if current == goal:
                return self._path_map_to_path(explored, current)

            # Look through current's neighbors that are unexplored.
            for neighbor in self.neighbors(current):
                if neighbor in explored:
                    continue
                
                # Add the neighbor to explored and push it to the frontier.
                explored[neighbor] = current
                frontier.push(neighbor)

        return None
        
    
    def bfs(self, start, goal):
        # Explored keeps track of where we've been and how we got there.
        explored = {}
        explored[start] = start
        
        # The frontier is created with a queue and the start is pushed to it.
        frontier = Queue()
        frontier.push(start)

        # Loop while the frontier is not empty and pop current of the frontier.
        while not frontier.is_empty:
            current = frontier.pop()

            # Check if current is the goal and if so, return the path.
            if current == goal:
                return self._path_map_to_path(explored, current)

            # Look through current's neighbors that are unexplored.
            for neighbor in self.neighbors(current):
                if neighbor in explored:
                    continue
                
                # Add the neighbor to explored and push it to the frontier.
                explored[neighbor] = current
                frontier.push(neighbor)

        return None
        
    
    def print_explored(self, explored):
        for k, v in explored.items():
            print(f"{k} : {v}")
            
    def __str__(self):
        lines = []
        for v, neighbors in self._adjacency_list.items():
            n_str = ", ".join(str(x) for x in sorted(neighbors))
            lines.append(f"{v}: {n_str}")
        return "\n".join(lines)
    
    def __repr__(self):
        return f"Graph({self._adjacency_list})"
    