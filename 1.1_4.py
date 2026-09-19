Day-1
PATTERNS
n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):    l-r=col
        print("*",end="")	u-d=row
    print("")

n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(j,end=" ")
    print("")
----------------
i is for lines
j is for print(*)

n=5
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
        
    print("")
--------------
n=5
for i in range(1,n+1,1):
    for j in range(1,i+2,1):
        print("*",end=" ")
        
    print("")
--------------

n=5
for i in range(1,n+1,1):
    for j in range(1,i+(i-1)+1,1):
        print("*",end=" ")
    print("")


even number pattern 
n=5
for i in range(1,n+1,1):
    for j in range(1,i+(i)+1,1):
        print("*",end=" ")
    print(" ")
------------------
n=5
for i in range(1,n+1,1):
    for j in range(1,(n-i)+1+1,1):
        print("*",end=" ")
    print(" ")
---------------
Decreasing odd order pattern
n=5
for i in range(1,n+1,1):
    for j in range(1,(n-i)+(n-i)+1+1,1):
        print("*",end=" ")
    print(" ")
----------------
Dec even number 
n=5
for i in range(1,n+1,1):
    for j in range(1,(n-i)+(n-i)+2+1,1):
        print("*",end=" ")
    print(" ")

