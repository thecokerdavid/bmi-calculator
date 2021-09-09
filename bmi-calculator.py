
"""

@author: David Coker
www.github.com/thecokerdavid

"""

height = input("enter your height in inches: ")
weight = input("enter your weight in pounds: ")

bmi = float(weight) * 703 / float(height) ** 2
bmi_approx = round(bmi, 1)
bmi_scale = ("BMI Scale (Adult):\n"
"Underweight = < 18.5\n"
"Normal weight = 18.5–24.9\n"
"Overweight = 25–29.9\n"
"Obesity = BMI of 30 or greater\n")

bmi_child_scale = ("BMI Scale (Children 2-20years):\n"
"Underweight = <14.6\n"
"Normal weight = 14.6–26.8\n"
"Risk of Overweight = 26.9–30.5\n"
"Overweight = BMI of 31 or greater\n")

print(f"Your BMI is {bmi_approx}, compare the value of your BMI to the scale.\n")

print(bmi_scale)
print(bmi_child_scale)
