x = int(input("Enter a number\n"))
flag = False
if x == 0 or x == 1:
    print(x,"is not a prime number\n")
elif x>1:
    for i in range(2,x):
        if(x %i ==0):
            flag = True
            break
if flag:
    print(x,"is not a prime number\n")
else:
    print(x,"is a prime number\n")
