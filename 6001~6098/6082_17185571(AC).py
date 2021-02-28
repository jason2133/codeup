a = int(input())

for i in range(1, a+1):
    i = str(i)
    a3 = i.count('3')
    a6 = i.count('6')
    a9 = i.count('9')
    a0 = a3 + a6 + a9
    
    if a0 == 0:
        print(i, end=' ')
    else:
        print(a0 * 'X', end = ' ')
    

