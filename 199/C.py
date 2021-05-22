N = int(input())
S = input()
Q = int(input())
lis = []
for i in range(Q):
  t,a,b = map(int,(input().split()))
  if t== 1:
    a = a -1
    b = b - 1
    t1 = S[a]
    t2 = S[b]
    tmp = ""
    tmp2 =""
    tmp3 =""
    if(a-1>0):
      tmp = S[:a-1]
    if(b+1 < N*2 ):
      tmp2 = S[b+1:]
    if(b-a-1>0): 
      tmp3 = S[a+1:b-a-1]
    S = tmp + t1 + tmp3 + t2 + tmp2
  else:
    ch = S
    tmp = S[0:N]
    tmp2 =ch[N:]
    S = tmp2 + tmp
    print(S)
print(S)         