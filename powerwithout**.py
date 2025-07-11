num = int(input("Enter a number\n"))
exp = int(input("enter the exponent\n"))
result = 1
count = 0

while count<exp:
    result*=num
    count+=1
print(f"{result}is the factorial of {num}\n");
