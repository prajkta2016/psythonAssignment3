def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number"))
result=factorial(n)
print("factorial of ",n," or ", n,"! is: ",result)