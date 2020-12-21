def ind(a, b):
    l = []
    n = []
    index = []
    for x in b:
        s = a.count(x)
        l.append(s)
    for x in b:
        for i in range(len(a)):
            if x == a[i]:
                n.append(i + 1)

    for j in range(len(l)):
        m = n[:l[j]]
        n = n[l[j]:]
        index.append(m)
    return index


def numb(x, new_min):
    for i in range(len(x)):
        l = []
        for j in range(len(x[i])):
            if x[i][j] > new_min[-1]:
                k = x[i][j]
                l.append(k)
        new_min.append(l[0])
    return new_min


with open("rosalind_sseq.txt") as file:
    l = []
    n = []
    p = []
    file = file.read()
    s = file.split()
    s = len(s[0])
    f = file.replace("\n", '')
    f = f.split(">")
    f.remove(f[0])
    for x in f:
        x = x[s - 1:]
        l.append(x)
    a = [x for x in l[0]]
    b = [x for x in l[1]]
    listed = ind(a, b)

    first = listed[0][0]
    new_min = [first]

    listed.remove(listed[0])

    final = numb(listed, new_min)
    print(*final)