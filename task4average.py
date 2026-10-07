A = list(map(int, input().split()))

summa = 0
count = 0
for x in A:
    if x % 3 == 0 and abs(x) % 10 == 1:
        summa += x
        count += 1

if count > 0:
    print(summa / count)
else:
    print("таких чисел нет")