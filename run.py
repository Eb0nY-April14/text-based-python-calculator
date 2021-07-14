
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
    #invalid_operator_result = 0
    if choice == 'g':
        num = float(input("Enter a number: "))
        result = num ** NUM_CONSTANT
        return result


answer = calculate_operation() 
print(f"The Result of your calculation is: {answer}" )       



