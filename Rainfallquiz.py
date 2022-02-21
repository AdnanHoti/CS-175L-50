# CS175
# Adnan Hoti
# rainfall.py
# Declare variables to hold the total rainfall,
# monthly rainfall, average rainfall (all float), the number
# of years, and the total number of months.

month = 0

Sum = 0

Years = int(input("Enter number of years: "))

while Years < 1 or Years > 3:

    Years = int(input("Enter number of years: "))

    if Years < 1 or Years > 3:

        print("Invalid years!")

for x in range(Years):

    print("Enter year", x+1," : ")

    for x in range(12):

        print("Enter Rainfall in month", x+1, ": ", end =' ')

        y = float(input())


        Sum = Sum + y

        month = month + 1

Average = Sum/month

months = Years * 12

print("Months:", months)

print("Total rainfall = ", Sum)

print("Average rainfall = ", Average)

#The End
