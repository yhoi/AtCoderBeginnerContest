n = int(input())
A = []
B = []
amin =0
bmin = 0
amin2 =0
bmin2 =0

for i in range(n):
    tmp = input().split()
    A.append(int(tmp[0]))
    B.append(int(tmp[1]))
    if i==0:
        amin = i
        bmin = i
    if A[i] < A[amin]:
       amin2 = amin
       amin = i
    if B[i] < B[bmin]:
        bmin2 = bmin
        bmin = i

if amin == bmin:
  
   if A[amin] > B[bmin2]:
       ans2 = A[amin]
   else:
       ans2 = B[bmin2]
   if A[amin2] > B[bmin]:
       ans3 = A[amin2]
   else:
       ans3 = B[bmin] 
   ans = [A[amin]+B[bmin],ans2,ans3]
   ans.sort()
   print(ans[0])            

else:
    if A[amin] > B[bmin]:
      print(A[amin])
    else: 
      print(B[bmin])        
