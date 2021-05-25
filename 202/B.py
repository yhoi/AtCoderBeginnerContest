S = input()
ans=[]
for i in range(len(S)):
    if S[i] == '6':
        ans.append('9')
    elif S[i] =="9":
        ans.append('6')
    else:
        ans.append(S[i])

ans.reverse()
for i in ans:
    print(i,end="")

        

