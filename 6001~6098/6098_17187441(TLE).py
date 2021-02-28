a=[[0 for j in range(11)]for i in range(11)]

for k in range(10):
    x=list(map(int,(input().split())))
    for l in range(10):
        a[k+1][l+1]=x[l]
        
m=2
n=2
while (a[m][n]!=2):
    a[m][n]=9
    if (a[m][n+1]==1 and a[m+1][n]==1) or (m==9 and n==9):
        break 
    if a[m][n+1]==0:
        n+=1
    elif a[m][n+1]==1 and (a[m+1][n]==0 or a[m+1][n]==2):
        m+=1            
a[m][n]=9 

for o in range(1,11):
    for p in range(1, 11):
        print(a[o][p],end=' ')
    print('')

