import random 

#initialization
name="" 
address=""
units_consumed = 0
bill_amount = 0
solar_writeoff = 0

# Accepting address, name and units of electricity consumed
name=input("Hello. Please enter your name: ")
address=input ("Your address now, please ")
units_consumed =int(input ("And how many units of electricity did you consume this month? "))

# solar test function
def solar_test():
    check =input ("Does your household have a solar panel? (Yes/No) ").lower()
    if check == "yes":
        solar_writeoff = 10
    else:
       solar_writeoff = 0


# Calculation
if units_consumed >= 1 and units_consumed <5 :
    #first 4 units cost 11 rupees per unit
    bill_amount = (units_consumed * 11)
elif units_consumed >= 5 and units_consumed <10:
    # units 5 to 9 are charged 14 rupees per unit
    bill_amount = (44 + ((units_consumed - 4)*14)) 
elif units_consumed >=10 and units_consumed <30:
    # units 10 to 29 are charged at 18 rupees per unit
    bill_amount = ((44+70) + (units_consumed - 9)*18)
else: 
    print ("error")

# Printing
solar_test()
bill_amount = bill_amount - ((solar_writeoff/100) * bill_amount)
print ("Hello, "+ name)
print ("\nYour electricity bill for this month is " + str(bill_amount))