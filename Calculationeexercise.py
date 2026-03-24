opearator = input("Please enter any operator it could be + , - , *, /: ")
num1 = float(input("Please enter x : "))
num2 = float(input("Please enter y : "))

if opearator == "+":
    result = num1 + num2
    print(round(result))

elif opearator == "-":
    result = num1 - num2
    print(round(result))

elif opearator == "*":
    result = num1*num2
    print(round(result))

elif opearator == "/":
    result = num1/num2
    print(round(result))

 