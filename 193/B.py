n = int(input())
i = 0 
ans = []
while(i < n):
    a,p,x = map(int,input().split())
    if(x - a> 0):
        ans.append(p)
    i = i +1

if(len(ans)==0):
    print(-1)
else:
  ans.sort()
  print(ans[0])

