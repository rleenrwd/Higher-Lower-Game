import random
import os
import time

# CREATE A LIST OF OBJECTS TO STORE PEOPLE TO COMPARE
people_to_compare = [
    {"name":"Rihanna", "title": "Musician", "followers": 100000},
    {"name":"Beyonce", "title": "Musician", "followers": 20000}, 
    {"name": "GaryVee","title" : "Motivator", "followers": 15990}, 
    {"name":"Donald Trump", "title": "President", "followers": 700000}, 
    {"name": "Usher", "title":"Musician", "followers": 1000000}, 
    {"name": "Lebron James", "title": "Basketball Player", "followers": 2000000}, 
    {"name": "Kim Kardashian", "title": "Business Woman", "followers": 5000000},
    {"name": "Robert Norwood", "title": "Software Engineer", "followers": 500}, 
    {"name": "Barack Obama", "title": "Former President", "followers": 4100300},
    {"name": "Cristiano Ronaldo", "title": "Footballer", "followers": 65200000},
    {"name": "Leo Messi", "title": "Footballer", "followers": 50500000},
    {"name": "Selena Gomez", "title": "Musician", "followers": 42100000},
    {"name": "The Rock", "title": "Actor and Wrestler", "followers": 39400000},
    {"name": "Kylie Jenner", "title": "Reality Star", "followers": 39300000},
    {"name": "Ariana Grande", "title": "Musician", "followers": 37600000},
    {"name": "Nike", "title": "Sportswear Brand", "followers": 30100000},
    {"name": "Justin Bieber", "title": "Musician", "followers": 29400000},
    ]

# GREET USER
def greet_user():
    print()
    print("Welcome to the Higher Lower Game!")
    
# CREATE SCREEN SPACE
def create_space():
    print("\n" * 2)
    
# RANDOMLY SELECT TWO PEOPLE FROM THE LIST TO COMPARE
def random_person(exclude=None):
    person = random.choice(people_to_compare)
    while person == exclude:
        person = random.choice(people_to_compare)
    return person

# FORMAT THE PEOPLES' FOLLOWER COUNT WITH A COMMA
def format_followers(followers):
    return format(followers, ",")

# CLEAR THE SCREEN (For Cross-Platform)
def clear_screen():
    time.sleep(2)

    if os.name == 'nt': # Windows
        os.system('cls')
    else:
        os.system('clear')

# INITIALIZE SCORE
score = 0

# INITIALIZE PERSON A/PERSON B
person_a = random_person()
person_b = random_person(exclude=person_a)

# FORMAT THE FOLLOWER COUNT
person_a_followers = person_a["followers"]
pa_formatted_followers = format_followers(person_a_followers)

person_b_followers = person_b["followers"]
pb_formatted_followers = format_followers(person_b_followers)

greet_user()
create_space()

print(f"Person A is: {person_a['name']}, a {person_a['title']} from the United States, with {pa_formatted_followers} followers.")

create_space()
print(f"Person B is: {person_b['name']}, a {person_b['title']} from the United States, with ____ followers.")

# MAIN GAME LOOP
while True:
    create_space()

    correct_answer = 'a' if person_a_followers > person_b_followers else 'b'

    user_guess = input("Who do you think has more followers? \nEnter either 'a' or 'b' or 'q' to quit: ").strip().lower()
    
    if user_guess == "a" and correct_answer == "a":
        print("THAT'S CORRECT!")
        score+=1
        print(f"YOUR SCORE IS: {score}")
        person_a = person_a
        person_a_followers = person_a["followers"]
        pa_formatted_followers = format_followers(person_a_followers)

        person_b = random_person(exclude=person_a)
        person_b_followers = person_b["followers"]
        pb_formatted_followers = format_followers(person_b_followers)

        print("RESETTING SCREEN")
        clear_screen()

        print(f"Person A is: {person_a['name']}, a {person_a['title']} from the United States, with {pa_formatted_followers} followers.")
        create_space()
        print(f"Person B is: {person_b['name']}, a {person_b['title']} from the United States, with ____ followers.")

    elif user_guess == "b" and correct_answer == "b":
        print("THAT'S CORRECT!")
        score+=1
        print(f"YOUR SCORE IS: {score}")
        person_a = person_b
        person_a_followers = person_a["followers"]
        pa_formatted_followers = format_followers(person_a_followers)

        person_b = random_person(exclude=person_a)
        person_b_followers = person_b["followers"]
        pb_formatted_followers = format_followers(person_b_followers)

        print("RESETTING SCREEN")
        clear_screen()

        print(f"Person A is: {person_a['name']}, a {person_a['title']} from the United States, with {pa_formatted_followers} followers.")
        create_space()
        print(f"Person B is: {person_b['name']}, a {person_b['title']} from the United States, with ____ followers.")

    elif user_guess == "q":
        print("YOU CHOSE TO QUIT. GOODBYE!")
        print(f"YOUR FINAL SCORE WAS: {score}")
        break
    else:
        print(f"That's INCORRECT!\nGAME OVER.\nYOUR FINAL SCORE WAS {score}")
        break