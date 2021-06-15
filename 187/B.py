N = int(input().split())
X = []
Y = []
r = 0
for i in range(N):
    x,y = int(input().split())
    X.append(x)
    Y.append(y)
for i in range(len(X)):
    for j in range(len(X)):
        if(i==j):
            continue
        r = int((Y[i]-Y[j]) / (X[i]-X[j]))