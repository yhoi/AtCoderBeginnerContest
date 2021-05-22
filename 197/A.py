S = input().split()

tmp = S[0]

for i in range(S.len):
  if(i == S.len):
    S[i]=tmp
   else:
     S[i]=S[i+1] 

print(S)