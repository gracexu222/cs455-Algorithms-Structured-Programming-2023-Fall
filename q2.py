class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root1 = self.find(i)
        root2 = self.find(j)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def connected_components(graph, n):
    ds = DisjointSet(n)
    for u in range(n):
        for v in graph[u]:
            ds.union(u, v)
    # Create a dictionary of connected components
    components = {}
    for i in range(n):
        root = ds.find(i)
        if root in components:
            components[root].add(i)
        else:
            components[root] = {i}
    return list(components.values())

def generate_graph(component_sizes):
    # Start assigning node numbers from 0
    start_node = 0
    graph = {}
    for size in component_sizes:
        for node in range(start_node, start_node + size):
            # Create a fully connected component
            graph[node] = set(range(start_node, start_node + size)) - {node}
        start_node += size
    return graph

def test_connected_components(component_sizes):
    # Generate the graph
    graph = generate_graph(component_sizes)
    # Flatten the graph keys to get the number of nodes
    n = max(graph.keys()) + 1
    # Find the connected components
    found_components = connected_components(graph, n)
    # Generate the expected results
    expected_components = []
    start_node = 0
    for size in component_sizes:
        expected_components.append(set(range(start_node, start_node + size)))
        start_node += size
    # Compare the results
    found_components = [set(component) for component in found_components]
    for found, expected in zip(sorted(found_components), sorted(expected_components)):
        assert found == expected, f"Components do not match: {found} != {expected}"
    print("All tests passed successfully.")

test_connected_components([10]*10)
test_connected_components([100, 500])
test_connected_components([250, 5, 10])
