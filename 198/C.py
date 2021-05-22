import math

r,x,y = map(int, input().split())
dis = math.sqrt(x**2+y**2)
if(dis==r):
    print(1)
elif(dis<=r*2):
  print(2)
else:
  print(math.ceil(dis/r))
