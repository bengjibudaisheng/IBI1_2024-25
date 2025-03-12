w=float(input("weight="))
h=float(input("height="))
BMI=w/h**2
# collect weight and height data, and calculate BMI
if BMI<18.5:
    print("Your BMI is ",BMI,", and you are considered underweight.")
elif BMI>30:
    print("Your BMI is ",BMI,", and you are considered obese.")
else:
    print("Your BMI is ",BMI,", and you are considered normal weight.")
# Based on the BMI range, output BMI and whether you should be considered underweight, normal weight, or obese.