
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
    invalid_operator_result = 0.0
    if choice == 'g':
        num = float(input("Enter a number: "))
        result = num ** NUM_CONSTANT
        return result
    else:
        num_1 = float(input("Enter your first number: "))
        num_2 = float(input("Enter your second number: "))    
        if choice == 'a':
        #num_1 = float(input("Enter your first number: "))
        #num_2 = float(input("Enter your second number: "))
            result = num_1 + num_2
            return result
        elif choice == 'b':
        #num_1 = float(input("Enter your first number: "))
        #num_2 = float(input("Enter your second number: "))
            result = num_1 - num_2
            return result
        else:
            return invalid_operator_result    


answer = calculate_operation() 
print(f"The Result of your calculation is: {answer}")       



