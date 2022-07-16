# ask the user some questions, if they get it right add +1 to the score
# print their result at the end of the program

print("Hello there! Welcome to my quiz")


# to ask user if they want to play or not. If they do, we proceed by asking them their name
playing = input("Do you want to play the game? Enter yes to continue: " ).lower()
if (playing) != "yes":
    quit()

print("Okay then, let's play. ")
name = input("Let's get to know each other. Enter your name please: ")
print ("hi "+name+"! The quiz pertains to military history, geopolitics, history, etc. For each correct answer you will recieve 1 mark. There is no negative marking "  )

# Creation of a variable to keep score and question from here and below
score = 0
total_questions = 0

# To whom does the R&AW report to?
answer = input("To whom does the R&AW report to? ").lower()
total_questions +=1
if answer == "pm" or answer == "prime minister":
    print("Correct!")
    score +=1
else:
    print("Incorrect")  


# Where is the Tibetian Government in exile located?
answer = input("Where is the Tibetian Government in exile located? ").lower()
total_questions +=1
if answer == "dharamshala":
    print("Correct!")
    score +=1
else:
    print("Incorrect")  

# Which party/group, also known as the Chinese Nationalists, established the Republic of China in Taiwan?
answer = input("Which party/group, also known as the Chinese Nationalists, established the Republic of China in Taiwan? ").lower()
total_questions +=1
if answer == "kuomintang" or answer == "kmt":
    print("Correct!")
    score +=1
else:
    print("Incorrect")  


# Often praised as an example of benevolent authoritarianism, who was the founding President of Singapore?
answer = input("Often praised as an example of benevolent authoritarianism, who was the founding President of Singapore? ").lower()
total_questions +=1
if answer == "lee kuan yew":
    print("Correct!")
    score +=1
else:
    print("Incorrect")  

# Which regiment of the Indian Army has its Regimental Centre in Ranikhet, India?
answer = input("Which regiment of the Indian Army has its Regimental Centre in Ranikhet, India? ").lower()
total_questions +=1
if answer == "kumaon regiment" or answer == "kumaon":
    print("Correct!")
    score +=1
else:
    print("Incorrect")  



# score processing and printing
print("Congratulations "+ name+"! " "You got "+ str(score)+ " points out of a possible "+ str(total_questions)+".")
print("You got "+ str((score/total_questions)*100)+ "%"+" of the answers correct.")