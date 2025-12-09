print("BMI calculator \n")
w=int(input("Enter your weight in KG:"))
h=float(input("Enter your height in meters"))
bmi=w/(h*h)
print("Your BMI is:", bmi)
if bmi<18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi<25:
    print("You are healthy weight")
else:
    print("You are obese")

