def exons(l, dna):
    for x in l:
        if x in dna:
            dna = dna.replace(x, "")
    return dna


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
with open("rosalind_splc.txt") as file:
    file = file.read()
    l = []
    c = []
    s = file.split()
    s = len(s[0]) - 1
    f = file.replace("\n", '')
    f = f.split(">")
    f.remove(f[0])
    for x in f:
        x = x[s:]
        b = x.replace('T', 'U')
        l.append(b)
    dna = l[0]
    l.remove(l[0])
    ex = exons(l, dna)
    split_three = [ex[index: index + 3] for index in range(0, len(ex), 3)]
    for x in split_three:
        for i in range(len(n)):
            if x == n[i][0]:
                c.append(n[i][1])
    c.remove("Stop")
    print("".join(x for x in c))
