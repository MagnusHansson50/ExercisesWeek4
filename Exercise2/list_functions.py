def last(l):
    i = len(l)
    return l[i - 1]

def cut_edges(l):
    i = len(l)
    l.pop(i - 1)
    l.pop(0)
    return l

def cut_edges_second(l):
    i = len(l)
    l_removed = []
    for x in range(1, (i - 1)):
        l_removed.append(l[x])
    return l_removed
