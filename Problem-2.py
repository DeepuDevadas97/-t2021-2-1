a=int(input("Input a = "))

if a%2 != 0:
    for i in range(1,a*2):
        if i%2 != 0:
            print(i,end=" ")
else:
    for i in range(1,a*2-1):
        if i%2 != 0:
            print(i,end=" ")
    
