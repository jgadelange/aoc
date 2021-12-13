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
    a.adj.add(bn)
    b.adj.add(an)

queue = Queue()
queue.put_nowait(["start"])
paths = []

while not queue.empty():
    path = queue.get_nowait()
    last = path[len(path)-1]
    node = tree.get_node(last)

    for adjn in node.adj:
        if adjn == "end":
            paths.append(path + [adjn])
            continue
        adj = tree.get_node(adjn)
        if not adj.is_small:
            queue.put_nowait(path + [adjn])
        elif adjn not in path:
            queue.put_nowait(path + [adjn])

print(len(paths))

f.close()
