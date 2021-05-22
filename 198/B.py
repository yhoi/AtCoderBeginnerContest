N = input()
result = "No"
for i in range(len(N)):
    if N == N[::-1]:
        result ='Yes'
        break
    N = "0"+ N

print(result)



