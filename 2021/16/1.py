f = open('./input', 'r')

total_v = 0
def generator(line):
    for c in line:
        for d in str(bin(int(c, base=16)))[2:].zfill(4):
            yield d


inp = "110100101111111000101000"


def alt_gen(line):
    for c in line:
        yield c


g1 = generator(f.readline().strip())
# g1 = generator("EE00D40C823060")
# g1 = generator("A0016C880162017C3686B18A3D4780")
# g1 = alt_gen(inp)


def take(gen, n):
    return (x for _, x in zip(range(n), gen))


def take_str(gen, n):
    return "".join(take(gen,n))


def take_to_int(gen, n):
    return int(take_str(gen, n), base=2)


class Parser:
    def __init__(self):
        self.total_v = 0

    def parse(self, g):
        v = take_to_int(g, 3)
        self.total_v += v

        print("v", v)

        t = take_to_int(g, 3)
        print("t", t)

        if t == 4:
            res = ""
            while True:
                leading = take_str(g, 1)
                res += take_str(g, 4)
                if leading == "0":
                    break

            return int(res, base=2)
        else:
            length_type = take_str(g, 1)
            print("I", length_type)
            if length_type == "0":
                l = take_to_int(g, 15)
                print("L", l)
                sub_gen = alt_gen(take_str(g, l))
                try:
                    while True:
                        print(self.parse(sub_gen))
                except:
                    pass
            else:
                sub_packets = take_to_int(g, 11)
                for i in range(sub_packets):
                    print(self.parse(g))


parser = Parser()
print(parser.parse(g1))
print(parser.total_v)

f.close()
