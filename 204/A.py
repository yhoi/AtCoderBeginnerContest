x,y = map(int,input().split())
if(x==y):
    print(x)
else:
    if(x==1):
        if(y == 2):
            print(0)
        else:
            print(2)
    if(x==2):
        if(y == 1):
            print(0)
        else:
            print(1)
    if(x==0):
        if(y == 1):
            print(2)
        else:
            print(1)