A1,A2,A3=map(int,input().split())

if(A1>A2):
    tmp =A1
    A1= A2
    A2 = tmp

if(A2>A3):
    tmp=A2
    A2=A3
    A3=tmp

if(A3>100):
  print('No')

result = (A3-A2)-(A2-A1)

if(result==0):
    print('Yes')
else:
    print('No')


//anwer

A1,A2,A3 = map(int,input().split())
ans = "No"
#(A1,A2,A3)
if A3-A2 == A2-A1:
    ans = "Yes"
#(A1,A3,A2)
if A2-A3 == A3-A1:
    ans = "Yes"
#(A2,A1,A3)
if A3-A1 == A1-A2:
    ans = "Yes"
print(ans)