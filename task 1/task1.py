
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

userInput = input("Enter choice (1/2/3/4):")

num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))

if userInput == '1' :
    print(num1 , '+' , num2 , '=', num1 + num2)
elif userInput == '2' :
    print(num1 , '-' , num2 , '=', num1 - num2) 
elif userInput == '3' :
    print(num1 , '*' , num2 , '=', num1 * num2) 
elif userInput == '4' :
   print( num1 , '/' , num2 , '=', num1 / num2)           

