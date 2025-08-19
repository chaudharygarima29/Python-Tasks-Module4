#factorial of a given number
n=int(input("Enter a number:"))
def factorial(x):
    if x==0 or x==1:
        return 1
    elif x<0:
        return "Factorial is not defined for negative numbers."
    else:
        return x*factorial(x-1)
c=factorial(n)
print("Factorial of",n,"is:",c)
