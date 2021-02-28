a, b, c = map(float, input().split())

d = (a * b * c) / 8 / 1024 / 1024

print("%.2f MB" % d)

