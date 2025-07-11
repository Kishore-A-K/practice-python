x = int(input("Enter number\n"))
count = 0;
y=x
if (x<10):
    print("No of digits:1\n")
    
else:
    while x > 0:
        count+=1
        x=x//10
    print(count,"is the number of digits for",y)

