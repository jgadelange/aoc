from itertools import islice, tee

f = open('./input', 'r')


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = {}
        self.dirs = {}
        self.parent = parent

    def get_size(self):
        return sum(
            dir.get_size() for dir in self.dirs.values()
        ) + sum(
            self.files.values()
        )


root = Dir("/")
current_dir = root

for command in f.read().split("$")[2:]:
    lines = [line.strip() for line in command.split("\n")]
    command = lines.pop(0)
    if command == "ls":
        for line in lines:
            if not line:
                continue
            a, b = line.split()
            if a == "dir":
                current_dir.dirs[b] = Dir(b, current_dir)
            else:
                current_dir.files[b] = int(a)
    elif "cd" in command:
        _, dirname = command.split()
        if dirname == "/":
            current_dir = root
        elif dirname == "..":
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.dirs[dirname]

dir_sizes = set()
stack = [root]
total = 0
while len(stack) != 0:
    current = stack.pop()
    size = current.get_size()
    dir_sizes.add(size)
    if size <= 100000:
        total += size
    stack.extend(current.dirs.values())

total_space = 70000000
root_size = root.get_size()
free_space = total_space - root_size

print(total)
print(next(size for size in sorted(dir_sizes) if free_space + size >= 30000000))

if __name__ == "__main__":
    pass
