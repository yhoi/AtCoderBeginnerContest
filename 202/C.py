N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = int(0)
i = int(0)
se = []
se2 =[]

while i < N:
    se.append(0)
    se2.append(0)
    i = i+1
i = int(0)
while i < N:
    se[A[i]-1]=se[A[i]-1]+1 
    check = B[C[i]-1]
    se2[check-1] = se2[check-1]+1 
    i = i+1
i = int(0)    
while i<N:
    ans = ans+(se[i]*se2[i]) 
    i = i+1

print(ans)