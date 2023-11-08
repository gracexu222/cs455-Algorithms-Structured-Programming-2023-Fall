class DisjointSet:
    def __init__(self, n):
        # Initialize singleton sets for each element
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, i):
        # Find the root of the set that contains element i with path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        # Merge the sets that contain x and y
        root_x = self.find(x)
        root_y = self.find(y)

        # Attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            # If ranks are same, then make one as root and increment its rank by one
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# Helper function to print connected components
def print_connected_components(ds, n):
    components = {}
    for i in range(n):
        root = ds.find(i)
        if root in components:
            components[root].add(i)
        else:
            components[root] = {i}
    for component in components.values():
        print(component)

# Test the implementation
ds = DisjointSet(7)
edges = [(0, 1), (2, 3), (3, 5), (4, 6)]

# Apply union operations for each edge
for x, y in edges:
    ds.union(x, y)

# Print the connected components
print_connected_components(ds, 7)
