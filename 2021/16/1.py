from functools import reduce

f = open('./input', 'r')

total_v = 0


def generate_bin(line):
    for c in line:
        yield c


def generator(line):
    for c in line:
        for d in str(bin(int(c, base=16)))[2:].zfill(4):
            yield d


def gt(g):
    return int(next(g) > next(g))


def lt(g):
    return int(next(g) < next(g))


def eq(g):
    return int(next(g) == next(g))


def product(g):
    return reduce(lambda acc, val: acc * val, g, 1)


class Parser:
    operator_map = {
        0: sum,
        1: product,
        2: min,
        3: max,
        5: gt,
        6: lt,
        7: eq,
    }

    def __init__(self, gen_or_line):
        if isinstance(gen_or_line, str):
            self.g = generator(gen_or_line)
        else:
            self.g = gen_or_line
        self.total_v = 0

    def take(self, n):
        return (x for _, x in zip(range(n), self.g))

    def take_str(self, n):
        return "".join(self.take(n))

    def take_to_int(self, n):
        return int(self.take_str(n), base=2)

    def parse(self):
        v = self.take_to_int(3)
        self.total_v += v

        t = self.take_to_int(3)

        if t == 4:
            return self.parse_literal()
        else:
            return self.calculate_operator(t)

    def calculate_operator(self, t):
        length_type = next(self.take(1))
        op = self.operator_map[t]
        if length_type == "0":
            return op(self.parse_total_length())
        else:
            return op(self.parse_num_packets())

    def parse_literal(self):
        res = 0
        while True:
            leading = next(self.take(1))
            res = (res << 4) + self.take_to_int(4)
            if leading == "0":
                break
        return res

    def parse_total_length(self):
        length = self.take_to_int(15)
        sub_parser = Parser(generate_bin(self.take_str(length)))
        try:
            while True:
                yield sub_parser.parse()
        except:
            pass
        self.total_v += sub_parser.total_v

    def parse_num_packets(self):
        sub_packets = self.take_to_int(11)
        for i in range(sub_packets):
            yield self.parse()


inp = f.readline().strip()
# inp = "D2FE28"

parser = Parser(inp)
result = parser.parse()
print("Part 1", parser.total_v)
print("Part 2", result)

f.close()
