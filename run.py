choice = input("""
Please Enter the operator you need for your calculation:
a for Add
b for Subtract
c for Multiply
d for Divide
e for Modulo
f for Power(Exponent)
g for Square Root
""")


def calculate_operation():
    NUM_CONSTANT = 0.5
    if choice == 'g':
        print("Doing the Square Root Calculation...\n")
        num = input("Enter a number:\n")
        val_num = validate_number(num)
        if validate_number(val_num):
            result = val_num ** NUM_CONSTANT
            print("Square Root Calculation completed Successfully.\n")
            return result
    else:
        validnum_1 = request_any_number()
        print("test", validnum_1)
        validnum_2 = request_any_number()
        print("test", validnum_2)
        if choice == 'a':
            print("Doing the Add Calculation...\n")
            result = float(validnum_1) + float(validnum_2)
            print(result)
            print("Add Calculation completed Successfully.\n")
            return result
        elif choice == 'b':
            print("Doing the Subtract Calculation...\n")
            result = num_1 - num_2
            print("Subtract Calculation completed Successfully.\n")
            return result
        elif choice == 'c':
            print("Doing the Multiply Calculation...\n")
            result = num_1 * num_2
            print("Multiply Calculation completed Successfully.\n")
            return result
        elif choice == 'd':
            print("Doing the Division Calculation...\n")
            result = num_1 / num_2
            print("Division Calculation completed Successfully.\n")
            return result
        elif choice == 'e':
            print("Doing the Modulo Calculation...\n")
            result = num_1 % num_2
            print("Modulo Calculation completed Successfully.\n")
            return result
        elif choice == 'f':
            print("Doing the Exponent Calculation...\n")
            result = num_1 ** num_2
            print("Exponent Calculation completed Successfully.\n")
            return result
        else:
            return "Null. You entered an invalid operator"


def request_any_number():
    num = input("Enter a number:\n")
    print(f"The number entered by the user is {num}")
    print(f"The data type of number entered by the user is {type(num)}")
    val_number = validate_number(num)
    if validate_number(num):
        print(f"The validated number is: {val_number}")
        print(type(val_number))  # num is a string not float
        return val_number
    else:
        request_any_number()
    # if validate_number(val_number):

    # if num:
    #    if validate_number(num):
    #        print(f"The validated number is: {val_number}")
    #        print(type(val_number))  # num is a string not float
    #        return val_number
    #    else:
    #        request_any_number()


def validate_number(number):
    try:
        val_num = float(number)
        print("The input entered by the user is Ok!")
        print(type(val_num))
        if type(val_num) == float:
            return val_num
    except ValueError:
        print("""Invalid input, NOT a number,
            Please try again!""")
        print(number)


print("Welcome to our text-based Calculator")
answer = calculate_operation()
print(f"Result of your calculation is {answer}")
