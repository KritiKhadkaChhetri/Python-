a = int(input("Enter your age: "))
#If statemnet no:1

if(a%2==0):
    print("You entered an even number.")
 
#end of if statement no:1

#If statement no:2
if (a >=18):
    print("You are an adult.")
    print("You are eligible to vote.")
    
elif (a<0):
    print("You entered an invalid age.")
    
elif (a==0):
    print("You are entering 0 which is not a valid age.")
    
else:
    print("You are a minor.")
    #end of if statement no:2
    
print("Thank you for using the age checker.")
