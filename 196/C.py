N = input()
N_len=len(N)
ans = int(0)
first_half =""
latter_half =""

for i in range(N_len):
  if i <N_len/2:
    first_half= first_half+(N[i])
  else:
    latter_half = latter_half+(N[i])

first_half_num = int(first_half) 
latter_half_num = int(latter_half)
digit = len(first_half)
if digit==1:
    ans = first_half_num
else:
   for i in range(10*(digit-1),first_half_num):
       ans = ans +1
print(ans+10*(digit-1))
    
