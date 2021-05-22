N = int(input())
A = input().split()
B = input().split()
A = [int(s) for s in A]
B = [int(s) for s in B]
a = int(0)
b = int(0)


for num in range(N):
   if num == 0:
       a = A[0]
       b = B[0]
   else:
       if A[num] > a:
         a = A[num]
       if  B[num] < b:
         b = B[num]

if(a>b):
    print(0)
else:
    answer = str(b -a +1)
    print(answer)
