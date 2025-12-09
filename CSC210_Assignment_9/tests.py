# tests.py
# Tests for your WeightedGraph.dijkstra(), edge_exists(), and path reconstruction.
# Do not modify the provided tests; add your own in the indicated section.
# Modified by: Nathan Huffman

import unittest
from weighted_graph import WeightedGraph


def print_path(path):
    for i, x in enumerate(path):
        end = "" if i == len(path) - 1 else " -> "
        print(f"{x}", end=end)
    print()


class TestDijkstraCityGraph1(unittest.TestCase):
    # DO NOT MODIFY THIS TEST CASE
    def test_city_graph_1(self):
        g = WeightedGraph()
        g.add_edge("Seattle", "Chicago", 2097)
        g.add_edge("Seattle", "Denver", 1331)
        g.add_edge("Seattle", "San Francisco", 807)
        g.add_edge("San Francisco", "Denver", 1267)
        g.add_edge("San Francisco", "Los Angeles", 381)
        g.add_edge("Los Angeles", "Denver", 1015)
        g.add_edge("Los Angeles", "Kansas City", 1663)
        g.add_edge("Los Angeles", "Dallas", 1435)
        g.add_edge("Denver", "Chicago", 1003)
        g.add_edge("Denver", "Kansas City", 599)
        g.add_edge("Kansas City", "Chicago", 533)
        g.add_edge("Kansas City", "New York", 1260)
        g.add_edge("Kansas City", "Atlanta", 864)
        g.add_edge("Kansas City", "Dallas", 496)
        g.add_edge("Chicago", "Boston", 983)
        g.add_edge("Chicago", "New York", 787)
        g.add_edge("Boston", "New York", 214)
        g.add_edge("Atlanta", "New York", 888)
        g.add_edge("Atlanta", "Dallas", 781)
        g.add_edge("Atlanta", "Houston", 810)
        g.add_edge("Atlanta", "Miami", 661)
        g.add_edge("Houston", "Miami", 1187)
        g.add_edge("Houston", "Dallas", 239)

        print("------cityGraph1------")
        print(g)  # uses __str__

        parents, distances = g.dijkstra("New York")

        # Are the distances from New York correct?
        self.assertEqual(distances["San Francisco"], 3057)
        self.assertEqual(distances["Los Angeles"], 2805)
        self.assertEqual(distances["Seattle"], 2884)
        self.assertEqual(distances["Denver"], 1790)
        self.assertEqual(distances["Kansas City"], 1260)
        self.assertEqual(distances["Chicago"], 787)
        self.assertEqual(distances["Boston"], 214)
        self.assertEqual(distances["Atlanta"], 888)
        self.assertEqual(distances["Miami"], 1549)
        self.assertEqual(distances["Dallas"], 1669)
        self.assertEqual(distances["Houston"], 1698)
        self.assertEqual(distances["San Francisco"], 3057)

        path = g.path_map_to_path(parents, "San Francisco")
        print("------cityGraph1 path------")
        print_path(path)

        # Shortest path should be: New York -> Chicago -> Denver -> San Francisco
        self.assertEqual(len(path), 4)
        self.assertEqual(path[0], "New York")
        self.assertEqual(path[-1], "San Francisco")

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g.edge_exists(last, current))
            last = current


class TestDijkstraCityGraph2(unittest.TestCase):
    # DO NOT MODIFY THIS TEST CASE
    def test_city_graph_2(self):
        g = WeightedGraph()
        g.add_edge("Seattle", "Chicago", 1737)
        g.add_edge("Seattle", "San Francisco", 678)
        g.add_edge("San Francisco", "Riverside", 386)
        g.add_edge("San Francisco", "Los Angeles", 348)
        g.add_edge("Los Angeles", "Riverside", 50)
        g.add_edge("Los Angeles", "Phoenix", 357)
        g.add_edge("Riverside", "Phoenix", 307)
        g.add_edge("Riverside", "Chicago", 1704)
        g.add_edge("Phoenix", "Dallas", 887)
        g.add_edge("Phoenix", "Houston", 1015)
        g.add_edge("Dallas", "Chicago", 805)
        g.add_edge("Dallas", "Atlanta", 721)
        g.add_edge("Dallas", "Houston", 225)
        g.add_edge("Houston", "Atlanta", 702)
        g.add_edge("Houston", "Miami", 968)
        g.add_edge("Atlanta", "Chicago", 588)
        g.add_edge("Atlanta", "Washington", 543)
        g.add_edge("Atlanta", "Miami", 604)
        g.add_edge("Miami", "Washington", 923)
        g.add_edge("Chicago", "Detroit", 238)
        g.add_edge("Detroit", "Boston", 613)
        g.add_edge("Detroit", "Washington", 396)
        g.add_edge("Detroit", "New York", 482)
        g.add_edge("Boston", "New York", 190)
        g.add_edge("New York", "Philadelphia", 81)
        g.add_edge("Philadelphia", "Washington", 123)

        print("------cityGraph2------")
        print(g)  # uses __str__

        parents, distances = g.dijkstra("Miami")

        # Are the distances from Miami correct?
        self.assertEqual(distances["Seattle"], 2929)
        self.assertEqual(distances["Chicago"], 1192)
        self.assertEqual(distances["Atlanta"], 604)
        self.assertEqual(distances["New York"], 1127)

        path = g.path_map_to_path(parents, "San Francisco")
        print("------cityGraph2 path------")
        print_path(path)

        # Shortest path should be:
        # Miami -> Houston -> Phoenix -> Riverside -> San Francisco
        self.assertEqual(len(path), 5)
        self.assertEqual(path[0], "Miami")
        self.assertEqual(path[-1], "San Francisco")

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g.edge_exists(last, current))
            last = current


# YOUR CODE HERE
# ADD YOUR OWN TEST CASE
# Prove that dijkstra() works correctly in your own test case,
# using the methods of WeightedGraph.
# You should make up your own graph and test it. Do not reuse cityGraph1/2.
# Look at the prior two tests as examples.
class TestDijkstraDarkSoulsGraph3(unittest.TestCase):
    def test_graph(self):
        g = WeightedGraph()
        g.add_edge("Firelink Shrine", "Undead Burg", 1000)
        g.add_edge("Firelink Shrine", "Undead Parish", 1000)
        g.add_edge("Firelink Shrine", "New Londo Ruins (Top)", 250)
        g.add_edge("Firelink Shrine", "The Catacombs", 1000)
        g.add_edge("Firelink Shrine", "The Depths", 1750)

        g.add_edge("Undead Burg", "Lower Undead Burg", 1000)
        g.add_edge("Undead Burg", "Undead Parish", 6000)
        g.add_edge("Undead Burg", "Darkroot Basin", 2000)

        g.add_edge("Undead Parish", "Sen's Fortress", 1000)
        g.add_edge("Sen's Fortress", "Anor Londo", 3000)
        
        g.add_edge("Anor Londo", "The Painted World of Ariamis", 2000)
        
        g.add_edge("Anor Londo", "The Duke's Archives", 2000)
        g.add_edge("The Duke's Archives", "Crystal Cave", 2000)
        g.add_edge("Crystal Cave", "Seath The Scaleless", 2000)
        
        g.add_edge("Undead Parish", "Darkroot Garden", 2000)
        g.add_edge("Darkroot Garden", "The Great Grey Wolf Sif", 4000)
        
        g.add_edge("Darkroot Basin", "Darkroot Garden", 2500)
        g.add_edge("Darkroot Basin", "The Valley of Drakes (North)", 1250)
    
        g.add_edge("The Valley of Drakes (North)", "New Londo Ruins (Bottom)", 500)
        g.add_edge("The Valley of Drakes (North)", "The Valley of Drakes (South)", 3000)
        
        g.add_edge("New Londo Ruins (Top)", "New Londo Ruins (Bottom)", 2500)
        g.add_edge("New Londo Ruins (Bottom)", "The Abyss", 500)

        g.add_edge("New Londo Ruins (Top)", "The Valley of Drakes (South)", 200)
        g.add_edge("The Valley of Drakes (South)", "Blighttown (Top)", 200)

        g.add_edge("Lower Undead Burg", "The Depths", 1250)
        g.add_edge("The Depths", "Blighttown (Top)", 2000)
        
        g.add_edge("Blighttown (Top)", "Blighttown (Bottom)", 3000)
        
        g.add_edge("Blighttown (Bottom)", "Quelaag's Domain", 1500)
        g.add_edge("Quelaag's Domain", "Demon Ruins", 1250)
        g.add_edge("Demon Ruins", "Lost Izalith", 3000)
        g.add_edge("Lost Izalith", "The Bed of Chaos", 4000)

        g.add_edge("Blighttown (Bottom)", "The Great Hollow", 1000)    
        g.add_edge("The Great Hollow", "Ash Lake", 2500)
        g.add_edge("Ash Lake", "The Ancient Dragon", 4000)

        g.add_edge("The Catacombs", "Tomb of The Giants", 2500)
        g.add_edge("Tomb of The Giants", "Gravelord Nito", 2500)

        print("\n------Dark Souls Map------")
        print(g)
        
        parents, distances = g.dijkstra("Firelink Shrine")

        # Are the distances from Firelink Shrine correct?
        self.assertEqual(distances["The Great Grey Wolf Sif"], 7000)
        self.assertEqual(distances["Seath The Scaleless"], 11000)
        self.assertEqual(distances["The Bed of Chaos"], 13400)
        self.assertEqual(distances["The Abyss"], 3250)
        self.assertEqual(distances["Gravelord Nito"], 6000)
        self.assertEqual(distances["The Painted World of Ariamis"], 7000)
        self.assertEqual(distances["The Ancient Dragon"], 11150)

        path = g.path_map_to_path(parents, "Quelaag's Domain")
        print("\n------Shortest Path to Quelaag's Domain------")
        print_path(path)

        # Shortest path should be:
        # Firelink Shrine -> New Londo Ruins (Top) -> The Valley of Drakes (South)
        # -> Blighttown (Top) -> Blighttown (Bottom) -> Quelaag's Domain
        self.assertEqual(len(path), 6)
        self.assertEqual(path[0], "Firelink Shrine")
        self.assertEqual(path[-1], "Quelaag's Domain")

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g.edge_exists(last, current))
            last = current


if __name__ == "__main__":
    unittest.main()
