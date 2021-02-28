a = int(input())
b = list(map(int, input().split()))
c = []
for i in range(1, 24):
    c.append(0)

for i in b:
    c[i-1] += 1

for i in c:
    print(i, end = " ")

