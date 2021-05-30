N,K = map(int,input().split())
AB = []
for i in range(N):
  AB.append(list(map(int,input().split())))

AB = sorted(AB, key=lambda x: x[0])

town = 0 
for i in range(len(AB)):
    if ((K+town)-AB[i][0]) <0:
       town += K
       print(town)
       exit()
    else:
       K -= AB[i][0]
       town += AB[i][0]
       K += AB[i][1] 
       if(i==len(AB)-1):
           town += K
           print(town)
           exit()