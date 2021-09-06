# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if weight/(height * height) < 18.5:
  print("You are underweight.")
elif 18.5 <= weight/(height * height) <= 25:
  print("You have a normal weight.")
elif 25 <= weight/(height * height) <= 30:
  print("You are slightly overweight.")
elif 30 <= weight/(height * height) <= 35: 
  print("You are obese.")
elif weight/(height * height) <= 35:
  print("You are clinically obese.")
else:
  pass
