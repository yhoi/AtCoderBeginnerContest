x,y = map(int,input().split())
if x > y:
    a = y
    b = x
else:
    a = x
    b = y

if((a+3) > b):
    print("Yes")
else:
    print("No")