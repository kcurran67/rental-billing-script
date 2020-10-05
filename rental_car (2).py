import sys

dailycharge = 60.00 # creating a global variable and naming it daily charge
weekcharge = 190.00 # creating a global variiable and naming it week charge
budgetcharge = 40.00 #
continueon = False


# will talke rentelcode imput from user and branch pases on that selection
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
# will get the rental periord  bases of branches and user
while continueon == False:


    if rentalCode == 'D' or rentalCode == 'd':

        rentalPeriod = input('Number of Days Rented:\n')
        rentalPeriod = int(rentalPeriod)
        break


    elif rentalCode == 'W' or rentalCode == 'w':
        rentalPeriod = input('Number of Weeks Rented:\n')
        rentalPeriod = int(rentalPeriod)
        break

    elif rentalCode == 'B' or rentalCode == 'b':
        rentalPeriod = input('Number of Days Rented:\n')
        rentalPeriod = int(rentalPeriod)
        break
    else:
        print('invalid input')
        rentalCode= input("(B)udget, (D)aily, or (W)eekly rental?\n")
continueon == True

odoStart = input("Starting Odometer Reading:\n")  # odemeter readin when car was first rented
odoEnd = input('Ending Odometer Reading:\n')  # odemeter reading when car was returned
totalMiles = int(odoEnd) - int(odoStart)

if rentalCode == 'B' or rentalCode == 'b':  # if user selected budget option will colext mile charge
    mileCharge = totalMiles * 0.25
    print(mileCharge)
averageDayMiles = totalMiles / rentalPeriod
averageWeekMiles = totalMiles / rentalPeriod


if rentalCode == 'D' or rentalCode == 'd' and averageDayMiles < 100:
    mileCharge = 0


elif rentalCode == 'D'or rentalCode == 'd' and averageDayMiles >= 100:
    extraMiles = averageDayMiles - 100

    mileCharge = extraMiles * 0.25
    print(mileCharge)


if rentalCode == 'W' or rentalCode == 'w' and (averageWeekMiles) < 900:  # under 900 no aditional charge
    mileCharge = 0


elif rentalCode == 'W' or rentalCode == 'w' and (averageWeekMiles) >= 900:  # over 900 aditional charge
    mileCharge =  100


if rentalCode == 'B' or rentalCode == 'b':  # base charg based on user input

    baseCharge = rentalPeriod * budgetcharge

if rentalCode == 'D'or rentalCode == 'd':

    baseCharge = rentalPeriod * dailycharge


elif rentalCode == 'W' or rentalCode == 'w':
    baseCharge = rentalPeriod * weekcharge




amount_due = float(baseCharge) + float(mileCharge)
amount_duef = "{:.2f}".format(amount_due)
print(amount_duef)

print('Youre rental code is ' + ' ' + str(rentalCode))
print('YOure rental period is'+ ' ' + str(rentalPeriod))
print('Youre starting odometer reading is' + ' ' + odoStart)
print('YOure ending odometer reading is' + ' ' + odoEnd)
print('Youre total miles are' + ' ' + str(totalMiles))

print('YOure total due is' + ' ' + '$' + str(amount_duef))
