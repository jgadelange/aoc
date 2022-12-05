import json
import operator
import re
import sys
import time
from functools import reduce
from itertools import combinations
from queue import PriorityQueue

f = open('./input', 'r')
starttime = time.time()

inp = [
    (
        line[:2] == "on",
        tuple(
            map(
                int,
                [x for x in re.search(r"x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line).groups()]
            )
        )
    )
    for line in f.readlines()
  ]


def contained(a, b):
    x, X, y, Y, z, Z = a
    u, U, v, V, w, W = b

    return (
       ((u <= x <= U) and (u <= X <= U)) and
       ((v <= y <= V) and (v <= Y <= V)) and
       ((w <= z <= W) and (w <= Z <= W))
   )


def x1(c):
    return c[0]
def x2(c):
    return c[1]
def y1(c):
    return c[2]
def y2(c):
    return c[3]
def z1(c):
    return c[4]
def z2(c):
    return c[5]


xyzs = [(x1, x2), (y1, y2), (z1, z2)]


def has_overlap(a, b):
    x, X, y, Y, z, Z = a
    u, U, v, V, w, W = b

    # return (
    #     x <= u <= X
    # )

    return (
        ((x <= u <= X) or (x <= U <= X) or (u <= x <= U) or (u <= X <= U)) and
        ((y <= v <= Y) or (y <= V <= Y) or (v <= y <= V) or (v <= Y <= V)) and
        ((z <= w <= Z) or (z <= W <= Z) or (w <= z <= W) or (w <= Z <= W))
    )


def has_overlap_dir(aa, bb, xyz):
    lower, caps = xyzs[xyz]
    a, A = lower(aa), caps(aa)
    b, B = lower(bb), caps(bb)

    return a <= b and B <= A


def has_z_overlap(a, b):
    return has_overlap_dir(a, b, 2)


def has_y_overlap(a, b):
    return has_overlap_dir(a, b, 1)


def has_x_overlap(a, b):
    return has_overlap_dir(a, b, 0)


xyzs_overlaps = [has_x_overlap, has_y_overlap, has_z_overlap]


def override(c, new, start=0):
    return tuple(
        new[i-start] if i in range(start, start+len(new)) else c[i]
        for i in range(6)
    )


def split(a, b, keep_overlap=True):
    if not has_overlap(a, b):
        print("NO OVERLAP KEEP BOTH")
        return {a, b}
    if keep_overlap:
        if contained(a, b):
            print("A IN B KEEB B")
            return {b}
        if contained(b, a):
            print("B IN A KEEB A")
            return {a}

    splits = {
        (0,0,0,0,0,0)
    }

    x, y, z = 0, 2, 4
    splits = method_name(a, b, splits, x)
    splits = method_name(a, b, splits, y)
    splits = method_name(a, b, splits, z)
    check_consistency(splits)


    if not keep_overlap:
        o = get_overlap(a, b)
        assert o in splits
        splits.remove(o)
        check_consistency(splits | {o})

    check_consistency(splits)

    return {
        s
        for s in splits
        if has_overlap(a,s) or has_overlap(b,s)
    }


def get_overlap(a, b):
    if not has_overlap(a, b):
        return None
    x, X, y, Y, z, Z = a
    u, U, v, V, w, W = b
    o = (
        max(x,u),
        min(X,U),
        max(y,v),
        min(Y,V),
        max(z,w),
        min(Z,W),
    )
    return o

def get_area(a, b):
    assert has_overlap(a,b)

    x, X, y, Y, z, Z = a
    u, U, v, V, w, W = b
    o = (
        min(x,u),
        max(X,U),
        min(y,v),
        max(Y,V),
        min(z,w),
        max(Z,W),
    )
    return o


def check_consistency(cubes, **context):
    for x in cubes:
        for xyz1, xyz2 in xyzs:
            assert xyz1(x) <= xyz2(x)

    for x, y in combinations(cubes, 2):
        if has_overlap(x, y):
            print("cubes", cubes)
            print("x,y", x, y)
            print("overlap", get_overlap(x, y))
            print(context)
            # print(split(x,y))
            assert False, "OVERLAP EXISTS"


def update(tup, index, value):
    return tuple(
        value if i == index else tup[i]
        for i in range(len(tup))
    )
        

def remove(aa, bb):
    # bb = get_overlap(aa, bb)
    # if not bb:
    #     return {aa}

    # if not has_overlap(aa, bb):
    #     return {aa}

    # print(f"Removing bb from aa", aa, bb)
    # print("overlap", get_overlap(aa, bb))
    cubes = {(tuple(None for _ in range(6)), (None, None, None))}
    for xyz in [0, 2, 4]:
        i = xyz//2
        lower, caps = xyzs[xyz//2]
        direction = "xyz"[xyz//2]
        a, A = lower(aa), caps(aa)
        b, B = lower(bb), caps(bb)

        if b <= a and A <= B:
            """
            A a------------A 
            B b------------B
            R --------------
            
            A -a----------a- 
            B b------------B
            R --------------
            """
            # print(direction, 1)
            cubes = {
                (override(s, (a, A), xyz), update(inside, i, False))
                for (s, inside) in cubes
            }
        elif A < b or B < a:
            """
            A a---A--------- 
            B ------b------B
            R a---A--------- 
            
            A ------a------A
            B b---B--------- 
            R ------a------A
            """
            cubes = {
                (override(s, (a, A), xyz), update(inside, i, True))
                for (s, inside) in cubes
            }
            # print(direction, 2)
            pass
            # cubes = {
            #     override(s, (a, A), xyz)
            #     for s in cubes
            # }
        elif a < b and B < A:
            """
            A a------------A 
            B ...b-----B....
            R a--b-----B---A
            """
            # print(direction, 3)
            cubes = reduce(operator.or_, ({
                (override(s, (a, b-1), xyz), update(inside, i, True)),
                (override(s, (b, B), xyz), update(inside, i, False)),
                (override(s, (B+1, A), xyz), update(inside, i, True)),
            } for (s, inside) in cubes))
        elif a < b and A == B:
            """        
            A a------------A 
            B ---b---------B
            R a--b---------A
            """
            # print(direction, 4)
            cubes = reduce(operator.or_, ({
                (override(s, (a, b-1), xyz), update(inside, i, True)),
                (override(s, (b, A), xyz), update(inside, i, False)),
            } for (s, inside) in cubes))
        elif a < b and A < B:
            """        
            A a--------A.... 
            B ...b---------B
            R a--b-----A---B
            """
            # print(direction, 4)
            cubes = reduce(operator.or_, ({
                (override(s, (a, b-1), xyz), update(inside, i, True)),
                (override(s, (b, A), xyz), update(inside, i, False)),
                # (override(s, (A+1, B), xyz), update(inside, i, False)),
            } for (s, inside) in cubes))
        elif a < b and A < B:
            """
            A a--------A.... 
            B ...b---------B
            R a--b-----A---B
            """
            # print(direction, 5)
            cubes = reduce(operator.or_, ({
                (override(s, (a, b-1), xyz), update(inside, i, True)),
                (override(s, (b, A), xyz), update(inside, i, False)),
            } for (s, inside) in cubes))
        elif a > b and B < A:
            """           
            A ...a---------A
            B b--------B.... 
            R b--a-----B---A
            """
            # print(direction, 6)
            cubes = reduce(operator.or_, ({
                (override(s, (a, B), xyz), update(inside, i, False)),
                (override(s, (B+1, A), xyz), update(inside, i, True)),
            } for (s, inside) in cubes))
        elif a == b and B < A:
            """
            A a------------A 
            B b--------B....
            R a--------B---A
            """
            # print(direction, 7)
            cubes = reduce(operator.or_, ({
                (override(s, (a, B), xyz), update(inside, i, False)),
                (override(s, (B+1, A), xyz), update(inside, i, True)),
            } for (s, inside) in cubes))
    # print("after_remove", cubes)
    # print(aa)
    # print(bb)
    # print("\n".join(str(x) for x in cubes))
    # print()
    # check_consistency({c for c, _ in cubes}, in_remove=1)
    # overlap = get_overlap(aa, bb)
    # count_overlap = count_all_on({overlap} if overlap else {})
    # count_new = count_all_on({c for c, inside in cubes if any(inside)})
    # count_old = count_all_on({aa})
    # assert count_overlap + count_new == count_old
    # assert not any(has_overlap(bb, c) for c, inside in cubes if any(inside))
    # print(aa)
    # print(bb)
    # print("\n".join(str(x) for x in cubes))
    # combine = dict()
    # for c, inside in cubes:
    #     if inside not in combine:
    #         combine[inside] = [c]
    #     else:
    #
    #         combine[inside].append(c)
    # if len(cubes)>8:
    #     print(len(cubes))
    #     print(cubes)
    #     print(aa, combine)
    #     exit()
    #
    # if len(cubes)>8:
    #     print(len(cubes))
    #     print(cubes)
    return {
        c for c, inside in cubes
        if any(inside)
    }



def progress_print(msg):
    pass
    # print(msg)


def method_name(aa, bb, cubes, xyz):
    lower, caps = xyzs[xyz//2]
    direction = "xyz"[xyz//2]
    
    a, A = lower(aa), caps(aa)
    b, B = lower(bb), caps(bb)

    if a == b and A == B:
        """
        A a------------A 
        B b------------B
        R a------------A
        """
        return cubes
    if A < b or B < a:
        """
        A a---A--------- 
        B ------b------B
        R a---A-b------B
        
        A ------a------A
        B b---B--------- 
        R b---B-a------A
        """
        print("no_overlap", direction)
        return cubes

    if a < b and A == B:
        """        
        A a------------A 
        B ---b---------B
        R a--b---------A
        """
        return reduce(operator.or_, ({
            override(s, (a, b-1), xyz),
            override(s, (b, A), xyz),

        } for s in cubes))
    elif a == b and B < A:
        """
        A a------------A 
        B b--------B....
        R a--------B---A
        """
        return reduce(operator.or_, ({
            override(s, (a, B), xyz),
            override(s, (B + 1, A), xyz),
        } for s in cubes))
    elif a < b and B < A:
        """
        A a------------A 
        B ...b-----B....
        R a--b-----B---A
        """
        return reduce(operator.or_, ({
            override(s, (a, b-1), xyz),
            override(s, (b, B), xyz),
            override(s, (B+1, A), xyz),
        } for s in cubes))
    elif b < a and A == B:
        """        
        A ---a---------A
        B b------------B 
        R b--a---------A
        """
        return reduce(operator.or_, ({
            override(s, (b, a-1), xyz),
            override(s, (a, A), xyz),

        } for s in cubes))
    elif a == b and A < B:
        """
        B a--------A....
        A b------------B 
        R a--------A---B
        """
        return reduce(operator.or_, ({
            override(s, (a, A), xyz),
            override(s, (A + 1, B), xyz),
        } for s in cubes))
    elif b < a and A < B:
        """
        A ...a-----A....
        B b------------B 
        R b--a-----A---B
        """
        return reduce(operator.or_, ({
            override(s, (b, a-1), xyz),
            override(s, (a, A), xyz),
            override(s, (A+1, B), xyz),
        } for s in cubes))
    elif a < b and A < B:
        """
        A a--------A.... 
        B ...b---------B
        R a--b-----A---B
        """
        return reduce(operator.or_, ({
            override(s, (a, b-1), xyz),
            override(s, (b, A), xyz),
            override(s, (A+1, B), xyz),
        } for s in cubes))
    elif b < a and B < A:
        """
        A ...a---------A
        B b--------B.... 
        R b--a-----B---A
        """
        return reduce(operator.or_, ({
            override(s, (b, a-1), xyz),
            override(s, (a, B), xyz),
            override(s, (B+1, A), xyz),
        } for s in cubes))

    print("WTF", direction, (a, A), (b, B), aa, bb)
    exit(1)

    return {
        split
        for split in cubes
        if lower(split) <= caps(split)
    }

def count_all_on(to_count):
    # check_consistency(to_count, count=1)
    #
    return sum(
        (X-x+1) * (Y-y+1) * (Z-z+1)
        for x, X, y, Y, z, Z in to_count
    )
    # return sum(
    #     len(list(_ for _ in range(x,X+1) for __ in range(y,Y+1) for ___ in range(z,Z+1)))
    #     for x, X, y, Y, z, Z in to_count
    # )

cubes_on = set()


def handle_add(cubes, to_add):
    overlapping = {
        c
        for c in cubes
        if has_overlap(c, to_add)
    }

    if len(overlapping) == 0:
        cubes.add(to_add)
        return cubes

    if any(contained(to_add, c) for c in cubes):
        return cubes

    contained_in_new = {
        c
        for c in cubes
        if contained(c, to_add)
    }
    if contained_in_new:
        cubes.difference_update(contained_in_new)
        # return cubes

    overlapping = {
        c
        for c in cubes
        if has_overlap(c, to_add)
    }
    if len(overlapping) == 0:
        # print("no_overlap")
        return cubes

    rest = cubes-overlapping
    # print(rest, overlapping)

    for c1 in overlapping:
        # overlap = get_overlap(c1, to_add)
        # count_before = count_all_on({c1})
        remove_result = remove(c1, to_add)
        # assert count_before - count_all_on({overlap}) == count_all_on(remove_result)
        rest.update(remove_result)
    rest.add(to_add)
    return rest


def handle_remove(cubes, to_remove):
    # if any(contained(to_remove, c) for c in cubes):
    #     print("new contained", new, cubes)
    #     return cubes
    contained_in_new = {
        c
        for c in cubes
        if contained(c, to_remove)
    }
    if contained_in_new:
        cubes.difference_update(contained_in_new)
        # return cubes

    overlapping = {
        c
        for c in cubes
        if has_overlap(c, to_remove)
    }
    # if len(overlapping) == 0:
    #     # print("no_overlap")
    #     return cubes

    rest = cubes-overlapping
    # print(rest, overlapping)

    x = {to_remove}

    for c1 in overlapping:
        # overlap = get_overlap(c1, to_add)
        # count_before = count_all_on({c1})
        remove_result = set()
        for xx in x:
            remove_result.update(remove(c1, xx))
        new_x = set()
        for xx in x:
            new_x.update(remove(xx, c1))
        # assert count_before - count_all_on({overlap}) == count_all_on(remove_result)
        rest.update(remove_result)
    return rest


def get_overlapping(cubes):
    return reduce(
        operator.or_,
        (
            {a, b}
            for a, b in combinations(cubes, 2)
            if has_overlap(a, b)
        ),
        set()
    )


for i, (put_on, current) in enumerate(inp):
    # check_consistency(cubes_on, start_loop=1)
    # print(put_on, current, len(cubes_on), cubes_on)
    print(i, put_on, len(cubes_on))
    if put_on:
        cubes_on = handle_add({c for c in cubes_on}, current)
        continue
    else:
        cubes_on = handle_remove({c for c in cubes_on}, current)
    # if put_on and any(contained(current, c) for c in cubes_on):
    #     continue
    # if put_on:
    #     found = False
    #     for c in cubes_on:
    #         if contained(c, current):
    #             found = True
    #             continue
    #     if found:
    #         cubes_on.remove(c)
    #         cubes_on.add(current)
    # if not any(has_overlap(c, current) for c in cubes_on):
    #     pass
    # else:
    new = set()
    # containedc = {
    #     c
    #     for c in cubes_on
    #     if contained(c, current)
    # }
    for c1 in cubes_on:
        # while cubes_on:
        #     c1 = cubes_on.pop()
        # rest = remove(c1, current)
        # if any(has_overlap(c, c1) for c in rest):
        #     print(":?")
        #     print(c1)
        #     exit()
        remove_result = remove(c1, current)
        new.update(remove_result)
        # check_consistency(rest, c1=c1, remove_result=remove_result, rest=rest)
        # print(rest)
        # overlap = get_overlap(c, current)
        # print(count_all_on({c}))
        # print(count_all_on({overlap}))
        # print(count_all_on(rest))
        # new.update(rest)
    cubes_on = new
    # check_consistency(cubes_on, middle_loop=1)

    if put_on:
        cubes_on.add(current)
    #     num_before = count_all_on(cubes_on)
    #     num_current = count_all_on({current})
    #     overlaps = [
    #         get_overlap(c, current)
    #         for c in cubes_on
    #     ]
    #     num_in_overlaps = [
    #         count_all_on({overlap})
    #         for overlap in overlaps
    #         if overlap
    #     ]
    #
    #     cubes_on = handle_add(cubes_on, current)
    #
    #     if num_before + num_current - sum(num_in_overlaps) != count_all_on(cubes_on):
    #         print(num_before)
    #         print(num_current)
    #         print(num_in_overlaps)
    #         print(count_all_on(cubes_on))
    #         raise Exception()
    #     assert num_before + num_current - sum(num_in_overlaps) == count_all_on(cubes_on)
    # else:
    #     new = set()
    #
    #
    #     check_consistency(new)
    #     pass





print(count_all_on(cubes_on))
print(2758514936282235)


print(f"Took {time.time()-starttime}s")
f.close()
