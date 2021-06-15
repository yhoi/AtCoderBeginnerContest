A,B = input().split()
sumA = 0
sumB = 0
for a in A:
    sumA += int(a)
for b in B:
    sumB += int(b)
if sumA > sumB :
    print(sumA)
else:
    print(sumB)