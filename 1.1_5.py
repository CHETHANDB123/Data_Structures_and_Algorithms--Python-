Day-2

n=5
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end="")
    for j in range(1,i+1,1):
        print("*",end='')

    print('')
--------------------------
n=5
for i in range(1,n+1,1):
    for j in range(1,(i-1)+1,1):
        print("-",end="")
    for j in range(1,(n-i+1)+1,1):
        print("*",end='')

    print('')
---------------------------
Equilateral Triangle
n=5
for i in range(1,n+1,1):
    for j in range(1,(n-i)+1,1):
        print("-",end='')
    for j in range(1,(i+i-1)+1,1):
        print("*",end='')
    print('')
--------------------------
Reverse Equilateral Triangle
n=5
for i in range(1,n+1,1):
    for j in range(1,(i-1)+1,1):
        print("-",end='')
    for j in range(1,(n-i+n-i+1)+1,1):
        print("*",end='')
    print('')
-------------------------

n=5
for i in range(1,n+1,1):
    for j in range(1,(i)+1,1):
        print("*",end='')
    print('')
n=4
for i in range(1,n+1,1):
    for j in range(1,(n-i+1)+1,1):
        print("*",end='')
    print('')
-------------------------
Diamond
n=5
for i in range(1,n+1,1):
    for j in range(1,(n-i)+1,1):
        print("-",end='')
    for j in range(1,(i+i-1)+1,1):
        print("*",end='')
    print('')
n=4
for i in range(1,n+1,1):
    for j in range(1,(i)+1,1):
        print("-",end='')
    for j in range(1,(n-i+n-i+1)+1,1):
        print("*",end='')
    print('')
