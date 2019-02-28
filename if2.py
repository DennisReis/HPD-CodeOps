age = int(input("Enter your age: "))
have_own_car = str(input("Do you own your own car?(y/n): "))

if age >= 21:
    if have_own_car == 'y':
        print ("You are over 21 years old and own your own car")
    else:
        print ("You are over 21 years old and you do NOT own your own car")
else:
   if have_own_car == 'y':
        print ("You are younger than 21 and own your own car")
   else:
        print ("You are younger than 21 and you do NOT own your own car")

