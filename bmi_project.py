# BMI = (weight in pounds x 703) / (height in inches x height in inches)
UNDERWEIGHT_BMI = 18.5
NORMAL_WEIGHT_BMI = 24.9
OVERWEIGHT_BMI = 29.9
OBESE_BMI = 34.9
SEVERELY_OBESE_BMI = 39.9

name = input("Enter your name: ")
weight_in_pounds = int(input("Enter your weight in pounds(lb): "))
height_in_inches = int(input("Enter your height in inches(in): "))

bmi = (weight_in_pounds * 703) / (height_in_inches * height_in_inches)

print(bmi)

if bmi > 0:
    if bmi < UNDERWEIGHT_BMI:
        print(f"{name}, you are underweight.")
    elif bmi <= NORMAL_WEIGHT_BMI:
        print(f"{name}, you are normal weight.")
    elif bmi < OVERWEIGHT_BMI:
        print(f"{name}, you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
    elif bmi < OBESE_BMI:
        print(f"{name}, you are obese.")
    elif bmi < SEVERELY_OBESE_BMI:
        print(f"{name}, you are severely obese.")
    else:
        print(f"{name}, you are morbidly obese.")
else:
    print("Enter valid input")
