import random


city_centers = {'tehran': 'tehran',
                'alborz':'karaj',
                'north rheine westfalia': 'duesseldorf',
                'west azerbayejan' : 'tabriz'} 

while True:
    random_generated = random.choice(list(city_centers))
    print("What is the center of: ",  random_generated)
    guess = input("Enter the city: ").strip()

    if guess == 'Quit'.lower():
       print("Goodbye!") 
    elif guess == city_centers[random_generated]:
       print("Yes, that is the correct answer!")
    else:
        print("Wrong Answer! the correct answer is: " + city_centers[random_generated])
