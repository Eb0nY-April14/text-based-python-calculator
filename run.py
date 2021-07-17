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
        num = input("Enter a number: ")
        validate_number(num)
        result = num ** NUM_CONSTANT
        return result
    else:
        num_1 = input("Enter your first number: ")
        validate_number(num_1)
        num_2 = input("Enter your second number: ")
        validate_number(num_2)
        if choice == 'a':
            result = num_1 + num_2
            return result
        elif choice == 'b':
            result = num_1 - num_2
            return result
        elif choice == 'c':
            result = num_1 * num_2
            return result
        elif choice == 'd':
            result = num_1 / num_2
            return result
        elif choice == 'e':
            result = num_1 % num_2
            return result
        elif choice == 'f':
            result = num_1 ** num_2
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
