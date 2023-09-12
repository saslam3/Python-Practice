#Magic 8-Ball
import random

name = "Saimah"

question = "Is my name Saimah"

answer = ""

random_number = random.randint(1, 9)

print(random_number)

if(random_number == 1):
  answer = "Yes - definitely."

elif(random_number == 2):
  answer = "It is decidedly so."

elif(random_number == 3):
  answer = "Without a doubt."

elif(random_number == 4):
  answer = "Reply hazy, try again."

elif(random_number == 5):
  answer = "Ask again later."

elif(random_number == 6):
  answer = "Better not tell you now."

elif(random_number == 7):
  answer = "My source say no"

elif(random_number == 8):
  answer = "Outlook not so good."

elif(random_number == 9):
  answer = "Very doubtful."

else:
  answer = "Error."

print(name + " asks: " + question)

print("Magic 8-Ball's answer: " + answer)


#Sals Shipping

weight = 1.5


#Ground Shipping
if(weight<=2):
  charge = float(weight*1.50)+20

elif(2<weight<=6):
  charge = float(weight*3.00)+20

elif(6<weight<=10):
  charge = float(weight*4.00)+20

else:
  charge = float(weight*4.75)+20

print("${:.2f}".format(charge))

#Ground Premium Shipping
Ground_Premium = 125

print("Ground Premium Price: ${:.2f}".format(Ground_Premium))

#Drone Shipping 
if(weight<=2):
  charge_drone = float(weight*4.50)

elif(2<weight<=6):
  charge_drone = float(weight*9.00)

elif(6<weight<=10):
  charge_drone = float(weight*12.00)

else:
  charge_drone = float(weight*14.25)

print("${:.2f}".format(charge_drone))