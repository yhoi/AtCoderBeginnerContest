N = int(input())
S = []
T = []
for i in range(N):
    s,t = input().split()
    S.append(s)
    T.append(int(t))

for i in range(N):
    for j in reversed(range(i+1, N)):
            # 1. 後ろから順に隣り合う要素を比較する。
            if T[j-1] > T[j]:
                # 2. 左が右の要素に比べ大きい場合交換する。
                T[j-1], T[j] =T[j], T[j-1]
                S[j-1], S[j] =S[j], S[j-1]

print(S[N-2])               
