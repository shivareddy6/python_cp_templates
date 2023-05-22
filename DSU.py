class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.size = [1]*(n+1)
        self.min, self.max = [*range(n+1)], [*range(n+1)]
        self.count = n

    def findPar(self, a):
        """Returns the identifier (parent) of the set to which a belongs to!"""
        if self.parent[a] == a:
            return a
        x = a
        while a != self.parent[a]:
            a = self.parent[a]
        while x != self.parent[x]:
            self.parent[x], x = a, self.parent[x]
        return a

    def union(self, a, b):
        """Join two sets that contain a and b. Returns True if they are of same set else False is returned"""
        a, b = self.findPar(a), self.findPar(b)
        if a != b:
            if self.size[a] > self.size[b]:
                a, b = b, a
            self.parent[a] = b
            self.size[b] += self.size[a]
            self.min[b] = min(self.min[a], self.min[b])
            self.max[b] = max(self.max[a], self.max[b])
            self.count -= 1
            return False
        return True

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count

dsu = DisjointSetUnion(4)
dsu.union(0, 2)
print(dsu.count_sets())