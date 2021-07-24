def choose_operator():
    """
    Requests input for choice of operator from the user,
    displays meaningful feedback to the user if invalid
    choice is made.
    """
    global choice
    choice = input(
                   "Please Enter the operator you need"
                   "for your calculation: \n"
                   "a for Add\n"
                   "b for Subtract\n"
                   "c for Multiply\n"
                   "d for Divide\n"
                   "e for Modulo\n"
                   "f for Power(Exponent)\n"
                   "g for Square Root\n")
    return choice


def calculate_operation():
    """
    Performs the relevant calculation based on the user's
    choice and returns the result to the calling code.
    """
    choose_operator()
    NUM_CONSTANT = 0.5
    if choice == "g":
        print("Doing the Square Root Calculation...\n")
        sqrt_num = request_any_number("a")
        result = sqrt_num ** NUM_CONSTANT
        print("Square Root Calculation completed Successfully.\n")
        return result
    else:
        num_1 = request_any_number("the first")
        num_2 = request_any_number("the second")
        my_choice = choice
        if my_choice == "a":
            print("Doing the Add Calculation...\n")
            result = num_1 + num_2
            print("Add Calculation completed Successfully.\n")
            return result
        elif my_choice == "b":
            print("Doing the Subtract Calculation...\n")
            result = num_1 - num_2
            print("Subtract Calculation completed Successfully.\n")
            return result
        elif my_choice == "c":
            print("Doing the Multiply Calculation...\n")
            result = num_1 * num_2
            print("Multiply Calculation completed Successfully.\n")
            return result
        elif my_choice == "d":
            print("Doing the Division Calculation...\n")
            result = num_1 / num_2
            print("Division Calculation completed Successfully.\n")
            return result
        elif my_choice == "e":
            print("Doing the Modulo Calculation...\n")
            result = num_1 % num_2
            print("Modulo Calculation completed Successfully.\n")
            return result
        elif my_choice == "f":
            print("Doing the Exponent Calculation...\n")
            result = num_1 ** num_2
            print("Exponent Calculation completed Successfully.\n")
            return result
        else:
            return "Null. You entered an invalid operator"


def request_any_number(pos):
    """
    Requests for number inputs from the user and handles the
    exceptions and displays meaningful feedback to the user on
    the source of the error and how to handle it.
    """
    while True:
        try:
            num = float(input(f"Enter {pos} number:\n"))
            return num
        except ValueError:
            print("Invalid input - NOT a number. \n"
                  "Please try again!")


"""
Accept user name and displays a personalised welcome message
to the user.
"""
your_name = input("(Optional) Please Enter your name: \n")
print(f"Welcome {your_name} to the Calculator5000")
answer = calculate_operation()
print(f"The Final Result of your calculation is {answer}")


"""
Asks the user if he wants to perform another operation and
if yes, repeats the app all over aagain and if no, displays
the final result and exits.
"""
response = input("Would you like to Perform another Calculation y/n?\n")
while response == "y" or response == "Y":
    my_new_answer = calculate_operation()
    print(f"The Final Result of your calculation is {my_new_answer}\n")
    response = input("Would you like to Perform another Calculation y/n?\n")
else:
    print(f"Thanks for using the Calculator5000 {your_name}, Goodbye!")
