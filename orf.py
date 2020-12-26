from Bio import SeqIO


def rev(dna):
    a = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([a[c] for c in reversed(dna)])


a = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''
listed = a.split()
n = []
for i in range(len(listed)):
    if i % 2 == 0:
        c = [listed[i], listed[i + 1]]
        n.append(c)

if __name__ == "__main__":
    with open("rosalind_orf.txt", "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            a = str(seq_record.seq)

            b = a.replace("T", "U")

    rb = rev(b)

    prt = []
    rna = [b, rb]
    Stop = ["UAA", "UAG", "UGA"]
    for x in rna:
        for i in range(len(b) - 2):
            if x[i:i + 3] == "AUG":
                start = x[i:-1]
                prt.append(start)

    for y in prt:
        split_three = [y[index: index + 3] for index in range(0, len(y), 3)]
        final = []
        l = []
        for x in split_three:
            for i in range(len(n)):
                if x == n[i][0]:
                    l.append(n[i][1])

        for i in range(len(l)):
            if l[i] == "Stop":
                print("".join(x for x in l[0:i]))
                break

