def choose_operator():
    global choice
    choice = input(
                    """Please Enter the operator you need for your calculation:\n """
                    "a for Add\n"
                    "b for Subtract\n"
                    "c for Multiply\n"
                    "d for Divide\n"
                    "e for Modulo\n"
                    "f for Power(Exponent)\n"
                    "g for Square Root\n")
    return choice


def calculate_operation():
    choose_operator()
    NUM_CONSTANT = 0.5
    if choice == "g":
        print("Doing the Square Root Calculation...\n")
        sqrt_num = request_any_number("a")
        result = sqrt_num ** NUM_CONSTANT
        print("Square Root Calculation completed Successfully.\n")
        return result
    else:
        num_1 = request_any_number("the_first")
        num_2 = request_any_number("the_second")
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
    while True:
        try:
            num = float(input(f"Enter {pos} number:\n"))
            return num
        except ValueError:
            print("Invalid input - NOT a number. \n"
                  "Please try again!")


your_name = input("Please Enter your name: \n")
print(f"Welcome {your_name} to the Calculator5000")
answer = calculate_operation()
print(f"The Final Result of your calculation is {answer}")

response = input("Would you like to Perform another Calculation y/n? ")
while response == "y" or response == "Y":
    my_new_answer = calculate_operation()
    print(f"The Final Result of your calculation is {my_new_answer}\n")
    response = input("Would you like to Perform another Calculation y/n? ")
else:
    print(f"Thanks for using the Calculator5000 {your_name}, Goodbye!")
