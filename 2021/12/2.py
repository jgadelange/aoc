from queue import Queue

f = open('./input', 'r')


class Node:
    def __init__(self, name):
        self.name = name
        self.adj = set()
        self.is_small = self.name == self.name.lower()

    def __str__(self):
        return f"{self.name} ({self.is_small}): adj: {self.adj}"


class Tree:
    def __init__(self):
        self.nodes = {}

    def get_node(self, name):
        return self.nodes.setdefault(name, Node(name))


tree = Tree()
for line in f.readlines():
    an, bn = [x.strip() for x in line.split("-")]
    a = tree.get_node(an)
    b = tree.get_node(bn)
    a.adj.add(b)
    b.adj.add(a)

queue = [(False, tree.get_node("start"), set())]
c = 0

while len(queue):
    small_node, node, visited = queue.pop()

    for adj in node.adj:
        if adj.name == "start":
            continue
        if adj.name == "end":
            c += 1
            continue
        if not adj.is_small:
            queue.append((small_node, adj, visited))
        elif adj.name not in visited:
            queue.append((small_node, adj, visited.union({adj.name})))
        elif not small_node:
            queue.append((True, adj, visited.union({adj.name})))

print(c)

f.close()
