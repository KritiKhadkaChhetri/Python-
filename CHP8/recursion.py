'''
factorial(5) = 5* 4* 3* 2* 1  
factorial(n) = n * factorial(n-1)
factorial(0) = 1

  '''
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to find factorial: "))
print("The factorial of", n, "is", factorial(n))
