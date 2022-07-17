name= input("Let's start. What's your name? ")
print("Hi", name, ". Welcome to this adventure!")

answer = input("You failed your second attempt to get into the NDA. You can either study for a third attempt or get an admission in the economics program of your local college. What do you do? Reattempt or College? ").lower()

if answer == "reattempt":
    answer = input("You have wasted more time in your preparation. You have 50 days remaining until the exam. You can go cover the whole syllabus or you can start solving papers. What do you do? Type syllabus to cover the syallabus, or type papers to solve papers: ").lower()
    if answer == "papers":
       answer = input("You solve the papers and you get through. You have 3 months to prepare for your interview. Do you start immediately or after a break? Type now to start immediately or type break to go on a vacation").lower()
    if answer == "now":
            answer = input("You get through into the NDA. You win")
            if answer == "break":
             print("you get through and you win")
    elif answer == "syllabus":
      print("You loose")
    else:
        print('Not a valid option. You lose.')

elif answer == "college":
    print ("You get admitted into the LU for Economics. You get frustrated looking at other people's success. You kill yourself because you're a fucking pussy")

else:
    print('Not a valid option. You lose.')

print("Thank you for playing my game,",name)