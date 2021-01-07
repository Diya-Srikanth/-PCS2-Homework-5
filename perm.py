from itertools import permutations
if __name__=="__main__":
    a = int(input())
    l=[]
    for i in range(1,a+1):
        l.append(i)
    perm = list(permutations(l))
    print(len(perm))
    for x in perm:
        print(*x)