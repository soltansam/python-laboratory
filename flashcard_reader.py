import sys
import random

if len(sys.argv) < 2:
    print(" supply a flash card file Please.")
    exit(1)

flashcard_file = sys.argv[1]
f = open(flashcard_file, "r")


ques_dictionary = {}

for sentence in f:
    entry = sentence.strip().split(",")
    question = entry[0]
    answer = entry[1]
    ques_dictionary[question] = answer

f.close()

print("Welcome to flashcard Game")
print("Type 'Q' to quit the Game! ")

while True:
    random_generated = random.choice(list(ques_dictionary))
    print(random_generated)
    guess = input("Enter the answer: ").lower().strip()

    if guess == 'Quit'.lower():
       print("Goodbye!") 
    elif guess == ques_dictionary[random_generated].lower():
       print("Yes, that is the correct answer!")
    else:
        print("Wrong Answer! the correct answer is: " + ques_dictionary[random_generated])
