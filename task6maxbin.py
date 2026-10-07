A = list(map(int, input().split()))

best = A[0]
for x in A:
    if bin(x).count('1') > bin(best).count('1'):
        best = x

print(best)