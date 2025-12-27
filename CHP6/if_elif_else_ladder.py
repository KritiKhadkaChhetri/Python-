a = int(input("Enter your age: "))
# Using if, elif, and else ladder to check age conditions
if (a >=18):
    print("You are an adult.")
    print("You are eligible to vote.")
    
elif (a<0):
    print("You entered an invalid age.")
    
elif (a==0):
    print("You are entering 0 which is not a valid age.")
    
else:
    print("You are a minor.")
    
print("Thank you for using the age checker.")
