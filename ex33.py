

def a(n,m):
    i = 0
    num = []
    while i < n:
        print("At the top i is %d"%(i))
        num.append(i)
        i = i + m
        print("Numbers now: ",num)
        print("At the bottom i is %d"%(i))
    print("The numbers: ")

    for s in num:
        print(s)

n,m = eval(input(">"))

a(n,m)

num = []
for i in range(0,n,m):
    print("At the top i is %d"%(i))
    num.append(i)
    
    print("Numbers now: ",num)
    print("At the bottom i is %d"%(i))

for s in num:
    print(s)
