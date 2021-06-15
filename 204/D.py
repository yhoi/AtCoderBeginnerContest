n,m = map(int,input().split())
su = n
A = []
for i in range(m):
    a = list(map(int,input().split()))
    A.append(a) 
A.sort()
print(A)
