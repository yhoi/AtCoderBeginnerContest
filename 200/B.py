import math
N,K = map(int,input().split())
result = str(N)
for i in range(K):
  if(N%200 == 0 ):
      N = math.ceil(N/200)
      result = str(N)
  else:
      result += str(200)
      N = int(result) 
print(result)