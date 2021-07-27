n = int(input("Input : "))

for i in range(1, n):
    for j in range(1, i+1):
        if i%2 == 0: 
            print(i-j+1, end=" ")
        else:
            print(j, end=" ")        
    print("")
    
for i in range(n, -1 , -1):
    for j in range(1, i+1):
        if i%2 == 0: 
            print(i-j+1, end=" ")
        else:
            print(j, end=" ")    
    print("")
