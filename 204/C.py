n = int(input())
T = list(map(int,input().split()))
o1 = 0
o2 = 0
for i in range(len(T)):
    if i ==0:
        o1 += T[i]
    else:
        if(o1<=o2):
            o1 += T[i]
        else:
            o2 += T[i]
if(o1>o2):
    print(o1)
else:
    print(o2)