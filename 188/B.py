n = int(input())
A = []
ans = 0
for i in range(2):
    a = list(map(int,input().split()))
    A.append(a)
for i in range(n):
    ans  += A[0][i] * A[1][i]
if ans == 0:
    print("Yes")
else:
    print("No")
  