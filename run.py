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
        num = float(input("Enter a number: "))
        validate_number(num)
        result = num ** NUM_CONSTANT
        print("Square Root Calculation completed Successfully.\n")
        return result
    else:
        num_1 = float(input("Enter your first number: "))
        validate_number(num_1)
        num_2 = float(input("Enter your second number: "))
        validate_number(num_2)
        if choice == 'a':
            print("Doing the Add Calculation...\n")
            result = num_1 + num_2
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


def validate_number(number):
    try:
        val = float(number)
        print("The input entered by the user is Ok!")
        return val
    except ValueError:
        print("""Invalid input, NOT a number,
              Please try again!""")


answer = calculate_operation()
print(f"Result of your calculation is {answer}")
