import networkx as nx

with open("rosalind_tree.txt") as file:
    file = file.read()
    f = file.splitlines()
    t = int(f[0])
    f.remove(f[0])
    a = t - len(f) - 1
    print(a)
