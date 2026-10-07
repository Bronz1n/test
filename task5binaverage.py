A = list(map(int, input().split()))

summa = 0
count = 0
for x in A:
    b = bin(x)[2:]
    if len(b) == 4:
        summa += x
        count += 1

if count > 0:
    print(summa / count)
else:
    print("таких чисел нет")