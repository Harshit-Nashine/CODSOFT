#Simple Calculator with input prompts by Harshit Nashine
#Fundamental Elements Used:  1.Variables, 2.Connditional Statements(if\else\elif),3. Basic Operators 
#Built-in Functions Used: 1.Input, 2.Data Types(integer\float)
def main():
print("Welcome to Simple Calculator!")

No1 = float(input(" Choose Your 1st Number: "))
No2 = float(input(" Choose Your 2nd Number: "))

print("Press 1 for Addition (+)\nPress 2 for Subtraction (-)\nPress 3 for Multiplication (*)\nPress 4 for Division (/)")

Choice = int(input(" Choose Your Operator from 1-4: "))

if Choice == 1:
     print("The 'Additon' of the given two numbers is: ", No1 + No2)
elif Choice == 2:
     print("The 'Subtraction' of the given two numbers is: ",No1 - No2)
elif Choice == 3:
     print("The 'Multiplication' of the given two numbers is: ",No1 * No2)
elif Choice == 4:
     print("The 'Division' of the given two numbers is: ",No1 / No2)
else:
     print("Invalid input, Please choose an operator from 1-4")

input("Press enter to Quit\Exit:")
     main()

