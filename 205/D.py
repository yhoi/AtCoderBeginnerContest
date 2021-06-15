N,Q = map(int,input().split())
A = list(map(int,input().split()))
K = []
for i in range(Q):
    ki = int(input())
    K.append(ki)

maxA =  max(A)
maxk = max(K)

sortK = K
sortK.sort()
Adic = {}
count =1
num =1
i = 0
j = 0

while num <= maxk:
    if j >= len(A):
       if num == sortK[i]:
           Adic[str(num)] =count
           i +=1
       num += 1 
    elif count < A[j]:
       if num == sortK[i]:
           Adic[str(num)] =count
           i +=1
       num += 1
    else:
        j += 1
    count += 1

for k in K:
    print(Adic[str(k)])