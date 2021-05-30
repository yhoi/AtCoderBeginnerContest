n = int(input())
A = list(map(int,input().split()))
i = 1
j = 0
ans = 0
key =[]
value = []
while(i<n):
  j = 0
  klength = len(key) -1
  for k in range(klength,0 ,-1):
    print(k)
    if key[klenght -k] == i:
      j = k
      ans = ans + value[k]
  key.append(i)
  value.append(0)
  while(j < i):
    ans = ans + (A[i] - A[j])**2
    value[i] =  value[i] + (A[i] - A[j])**2
    j = j +1
  
  i = i +1
print(ans)  
