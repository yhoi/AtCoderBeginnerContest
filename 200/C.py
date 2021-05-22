import math
N = int(input())
A = input().split()
A = [int(s) for s in A]
result = int(0)
key = list()
num = int(1)
for i in range(N): 
  re = int(1)  
  for j in A[num+1:]:
    if(((A[num]-j)%2)== 0 or ((A[num]-j)%5)== 0):
        result = result +1
        key.append(re)
    re =re+1
  if(len(key)>0):
      result = result +  math.factorial(len(key))
      for r in key:
        del A[r]
      key = list()
      num = int(1)
      print(A)
  else:
      num = num+1  
   
print(str(result))
    
