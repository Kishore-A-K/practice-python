def factorial(n):
    i = 1
    result = 1
    while ( i<=n):
        result *= i
        i+=1
    return result

x = int(input("Enter a number\n"))
y = factorial(x)
print(f"{y} is the value\n")
