from Bio import SeqIO


def lcsq(a, b):
    m, n = len(a), len(b)
    p = [[0] * (n + 1) for _ in range(m + 1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                p[i + 1][j + 1] = 1 + p[i][j]
            else:
                p[i + 1][j + 1] = max(p[i + 1][j], p[i][j + 1])
    lcs = ""
    while m * n != 0:
        if p[m][n] == p[m - 1][n]:
            m -= 1
        elif p[m][n] == p[m][n - 1]:
            n -= 1
        else:
            lcs += a[m - 1]
            m -= 1
            n -= 1

    s = lcs[::-1]
    return s


if __name__ == "__main__":
    strings = []
    with open("rosalind_lcsq.txt") as file:
        for info in SeqIO.parse(file, "fasta"):
            strings.append(info.seq)
    a, b = strings

    print(lcsq(a, b))
