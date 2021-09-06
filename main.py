# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if weight/(height**2) < 18.5:
  print("You are underweight.")
elif 18.5 <= weight/(height**2)  <= 25:
  print("You have a normal weight.")
elif 25 <= weight/(height**2)  <= 30:
  print("You are slightly overweight.")
elif 30 <= weight/(height**2)  <= 35: 
  print("You are obese.")
elif weight/(height**2)  <= 35:
  print("You are clinically obese.")
else:
  pass
