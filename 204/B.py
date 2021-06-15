n = int(input())
A = list(map(int,input().split()))
su=0
for a in A:
    if(a>10):
        su += a-10
        
print(su)