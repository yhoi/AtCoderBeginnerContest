import math
n = int(input())
answer = int(0)
keta = int(1)
while(True):
  if(n/(1000**keta)>=1):
    tmp = math.floor(n/(1000**keta))
    num = n - (tmp*(1000**keta)) +1
    answer = answer + (num*keta) + ((1000**keta-1)-1)
    keta = keta +1
  else:
      break  
print(answer)
