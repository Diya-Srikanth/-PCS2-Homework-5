from Bio import SeqIO


def edges(s, n):
    l = []
    for i in range(len(s)):
        for j in range(len(s)):
            if j != i:
                if s[i][:3] == s[j][-3:]:
                    print(n[j], n[i])
    return ''
if __name__ == "__main__":
    strings = []
    serial = []
    with open("rosalind_grph.txt") as file:
        for info in SeqIO.parse(file, "fasta"):
            strings.append(info.seq)
            serial.append(info.name)

    print(edges(strings, serial))
