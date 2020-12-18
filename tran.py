def trans(l):
    c=0
    a = l[0]
    b = l[1]
    for i in range(len(a)):
        if a[i]=="A" and b[i] =="G":
            c+=1
        elif a[i]=="G" and b[i] =="A":
            c+=1
        elif a[i]=="T" and b[i] =="C":
            c+=1
        elif a[i]=="C" and b[i] =="T":
            c+=1
    return c
def transverse(l):
    c=0
    a = l[0]
    b = l[1]
    for i in range(len(a)):
        if a[i]=="A" and b[i] =="C":
            c+=1
        elif a[i]=="C" and b[i] =="A":
            c+=1
        elif a[i]=="G" and b[i] =="T":
            c+=1
        elif a[i]=="T" and b[i] =="G":
            c+=1
        elif a[i]=="C" and b[i] =="G":
            c+=1
        elif a[i]=="G" and b[i] =="C":
            c+=1
        elif a[i]=="A" and b[i] =="T":
            c+=1
        elif a[i]=="T" and b[i] =="A":
            c+=1
    return c
with open("rosalind_tran.txt", 'r') as file:
    l = []
    file = file.read()
    s = file.split()
    s = len(s[0])
    f = file.replace("\n", '')
    f = f.split(">")
    f.remove(f[0])
    for x in f:
        x = x[s-1:]
        l.append(x)
    transition = trans(l)
    transversion = transverse(l)
    y = int(transition)/int(transversion)
    ratio = (round(y,11))
    print(ratio)