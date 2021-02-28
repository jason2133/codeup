h,w=map(int,(input().split()))
a=[[0 for j in range(w+1)]for i in range(h+1)]

n=int(input())
for k in range(n):
    l,d,x,y=map(int,(input().split()))
    for m in range(l):
        if d==0:
            a[x][y+m]=1
        else:
            a[x+m][y]=1

for o in range(1,h+1):
    for p in range(1,w+1):
        print(a[o][p],end=' ')
    print('')
