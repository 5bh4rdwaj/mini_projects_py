# program to generate a number at random and track the number of attempt it takes the user to guess it.

# first, we import the "random" module, which comes prebuilt in the py libraries
import random

top_of_range = input("Type a number: ")

#checking to see if input was a number greater than 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
   
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()


# variable to store a random number b/w the lower limit x and upper limit top_of_range (x,top_of_range)
random_number = random.randint(0,top_of_range)
guess = 0


# main stuff
while True:
    guess +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it! The number generated was "+ str(random_number))
        break
    elif user_guess < random_number:
            print("You were below the number!")
    else:
        print("You were above the number!")




#to print how many guesses it took for the user to land at the answer
print("You got it in",guess,"guesses")
#the above line is replacement to: print("You got it in "+ str(guesses)+" guesses")

# End of program
