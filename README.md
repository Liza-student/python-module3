# python-module3
# factorial:
 def factorial(n):
Defines a function named factorial that takes one argument n.
result = 1
Initializes a variable result to 1. This will hold the running product.
 for i in range(1, n + 1):
Starts a loop from 1 to n (inclusive).

range(1, n + 1) ensures the loop includes n itself.
 result *= i
In each loop iteration, multiplies result by the current value of i.

This step builds the factorial by computing:
1 × 2 × 3 × ... × n
return result
Once the loop is finished, returns the final factorial value.

#Task3
#math calculation:
import math
Imports Python’s built-in math module to access mathematical functions like sqrt, log, and sin.
num = float(input("enter a number:"))
Prompts the user to enter a number.

Converts the user input from a string to a floating-point number (float) and stores it in num.
if num <= 0:
Checks if the entered number is less than or equal to zero.

This is necessary because:

The square root and natural logarithm of zero or negative numbers are not defined in the set of real numbers.
 print("please enter a number greater than zero.")
If the input number is less than or equal to zero, it prints an error message asking for a positive number.
 else:
If the number is greater than zero, the program proceeds with the calculations.

Prints the calculated values formatted nicely:
Square root value
Natural logarithm value
Sine value



