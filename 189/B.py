n,x = map(int,input().split())
ans = -1
s = 0
for i in range(n):
  v,p = map(int,input().split())
  s += v*p
  if x*100 < s:
    ans = (i+1)
    break

print(ans)    