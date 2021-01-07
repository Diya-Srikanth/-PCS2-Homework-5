from Bio import SeqIO
def dist(s1, s2):
    dist = (sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1))) / len(s1))

    return dist


def matrix(a):
    dp = [[0 for i in range(len(string))] for j in range(len(string))]
    for i in range(len(string)):
        for j in range(len(string)):
            change = (dist(string[i], string[j]))
            change = format(change, '.5f')
            dp[i][j] = change
    return dp


if __name__ == '__main__':
    string = []
    with open("rosalind_pdst.txt") as file:
        for info in SeqIO.parse(file, "fasta"):
            string.append(info.seq)
    l = (matrix(string))
    for x in l:
        print(*x)
