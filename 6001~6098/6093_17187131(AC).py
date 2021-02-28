a = int(input())
b = list(map(int, input().split()))

c = b[::-1]

for i in c:
    print(i, end = " ")

