# Create a custom module named calculator with functions for addition, subtraction, 
# multiplication, and division. Import it and use its functions in another program

import Calculator
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))

print("Addition: ",Calculator.add(a,b))
print("Subtrsction: ",Calculator.sub(a,b))
print("Multiplication: ",Calculator.mul(a,b))
print("Division: ",Calculator.div(a,b))

