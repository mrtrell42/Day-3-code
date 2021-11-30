weight = float(input("enter your weight: "))
height = float(input("enter your height: "))
bmi = round(weight / (height ** 2))
print(bmi)

if (bmi == 0):
    print('underwight')
elif (bmi > 1 and bmi <24):
    print("no way")        
elif (bmi > 25 and bmi <33):
    print('you are obese')
else:
    print("You are a litle unhealthy ")
