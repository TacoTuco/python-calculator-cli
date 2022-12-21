print("M = Multiply. D = Divide. A = Add. S = Subtract")
choice = input("Let's calculate something, enter what you'd like to do (M, D, A, S): ")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
if choice.upper() == "M":
    multiply = first_number * second_number
    print(str(first_number) + " * " + str(second_number) + " = " + str(multiply))
elif choice.upper() == "D":
    divide = first_number / second_number
    print(str(first_number) + " / " + str(second_number) + " = " + str(divide))
elif choice.upper() == "A":
    add = first_number + second_number
    print(str(first_number) + " + " + str(second_number) + " = " + str(add))
elif choice.upper() == "S":
    subtract = first_number - second_number
    print(str(first_number) + " - " + str(second_number) + " = " + str(subtract))
more = input("Need to calculate something else? Y or N: ")
if more.upper() == "Y":
    i = 1
    while i == 1:
        choice = input("Okay, great! Enter what you'd like to do (M, D, A, S): ")
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        if choice.upper() == "M":
            multiply = first_number * second_number
            print(str(first_number) + " * " + str(second_number) + " = " + str(multiply))
        elif choice.upper() == "D":
            divide = first_number / second_number
            print(str(first_number) + " / " + str(second_number) + " = " + str(divide))
        elif choice.upper() == "A":
            add = first_number + second_number
            print(str(first_number) + " + " + str(second_number) + " = " + str(add))
        elif choice.upper() == "S":
            subtract = first_number - second_number
            print(str(first_number) + " - " + str(second_number) + " = " + str(subtract))
        more = input("Need to calculate something else? Y or N: ")
        if more.upper() == "N":
            i = 0
            print("No problem. Have a great day!")
else:
    print("No problem. Have a great day!")



