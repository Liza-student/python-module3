import math
num = float(input("enter a number:"))
if num <=0:
    print("please enter a number greater than zero.")
else:
    square_root = math.sqrt(num)
    natural_log = math.log(num)
    sine_value = math.sin(num)

    print(f"square root:{square_root}")
    print(f"natural logarithm:{natural_log}")
    print(f"sine:{sine_value}")