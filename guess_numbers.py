# program to generate a number at random and track the number of attempt it takes the user to guess it.

# first, we import the "random" module, which comes prebuilt in the py libraries
import random

top_of_range = input("Type a number: ")

#checking to see if input was a number greater than 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()



# variable to store a random number b/w the lower limit x and upper limit top_of_range (x,top_of_range)
random_number = random.randint(-2,top_of_range)
print(random_number)