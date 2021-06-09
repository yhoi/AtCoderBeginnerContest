n = int(input())
gameNum = 2 **(n)
halfnum = int(gameNum/2)

A = list(map(int,input().split()))
firsthalf = A[0:halfnum]
secondhalf = A[halfnum: gameNum]
firsthalf.sort()
secondhalf.sort()
if (firsthalf[halfnum-1]>secondhalf[halfnum-1]):
    Anum = A.index(secondhalf[halfnum-1])
    print(Anum+1)
else:
    Anum = A.index(firsthalf[halfnum-1])
    print(Anum+1)