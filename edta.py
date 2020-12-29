import numpy as nx
from Bio import SeqIO


def edit(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])
    print(dp[m][n])

    a, b = "", ""
    i, j = 0, 0
    i, j = len(str1), len(str2)
    while (i>0 and j>0):
        x = dp[i][j-1]
        y = dp[i-1][j]
        z = dp[i-1][j-1]
        min_ = min(x,y,z)
        if dp[i][j]==min_:
            a = str1[i-1]+a
            b = str2[j-1]+b
            i -= 1
            j -= 1
        else:
            if (min_==x and min_==y) or (min_!=x and min_!=y):
                a = str1[i-1]+a
                b = str2[j-1]+b
                i -= 1
                j -= 1
            elif min_!=x and min_==y:
                a = str1[i-1]+a
                b = "-"+b
                i -= 1
            elif min_==x and min_!=y:
                a = "-"+a
                b = str2[j-1]+b
                j -= 1
    print(a)
    print(b)
    return ""
if __name__ == "__main__":
    strings=[]
    with open("rosalind_edta (2).txt") as file:
        for info in SeqIO.parse(file, "fasta"):
            strings.append(info.seq)
    str1 , str2 = strings
    print(edit(str1, str2, len(str1), len(str2)))