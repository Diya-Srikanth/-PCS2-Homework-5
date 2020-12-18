with open("rosalind_hamm.txt", 'r') as file:
    file = file.read()
    f = file.splitlines()
    l = []
    a = [str(i) for i in f[0]]
    b = [str(i) for i in f[1]]
    for j in range(len(a)):
        if a[j] != b[j]:
            l.append(a[j])
    print(len(l))
