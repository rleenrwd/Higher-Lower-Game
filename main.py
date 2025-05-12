import random

print("Welcome to the Higher Lower Game!")
print("In this game, you must try to guess which famous person has more followers than the other.")
print("The goal is to get as many correct and accumulate the highest score.")
print("Get one wrong and the game is over...")

# ASK USER TO PLAY THE GAME
play_game_or_quit = input("Are you ready to start? Type 'yes' to start or 'q' to quit: ").lower()

score = 0

# CREATE A LIST OF OBJECTS TO STORE PEOPLE TO COMPARE
people_to_compare = [{"name":"Rihanna", "title": "Musician", "followers": 1000000},{"name":"Beyonce", "title": "Musician", "followers": 2000}, {"name": "GaryVee","title" : "Motivator", "followers": 15990}, {"name":"Donald Trump", "title": "President", "followers": 7000000}, {"name": "Usher", "title":"Musician", "followers": 10000000}, {"name": "Lebron James", "title": "Basketball Player", "followers": 20000000}]

# RANDOMLY CHOOSE A PERSON FROM THE LIST, TO COMPARE
def choose_random_person(list):
    """Randomly chooses and returns two people from the list, inside a tuple"""
    new_person_one = random.choice(list)
    new_person_two = random.choice(list)

    if new_person_one["name"] == new_person_two["name"]:
        new_person_two = random.choice(list)

    return new_person_one, new_person_two

def create_screen_space():
    """Creates screen space using print statements"""
    print()
    print()
    print()
    print()
    print()
    print()
    print()


# CREATE TWO PEOPLE
person_one, person_two = choose_random_person(people_to_compare)

create_screen_space()

# DISPLAY THE PEOPLE TO THE USER
print(f"Person A is: {person_one["name"]}, who is a famous {person_one["title"]}, from the United States")

create_screen_space()

print(f"Person B is: {person_two["name"]}, who is a famous {person_two["title"]}, from the United States")

create_screen_space()

# ASK THE USER WHICH PERSON THEY THINK HAS MORE FOLLOWERS
user_choice = input("Who do you think has more followers? Type 'a' or 'b': ").lower()


# CHECK TO SEE IF THE USER'S CHOICE IS CORRECT OR NOT

# END GAME IF THE USER IS INCORRECT

# INCREMENT THE SCORE VARIABLE IF THE USER IS CORRECT 

# PICK A NEW PERSON FOR THE USER TO COMPARE THE PREVIOUS PERSON THEY GOT CORRECT TO















# if person_one == person_two:
#     person_two = choose_random_person(people_to_compare)
# elif person_one["followers"] > person_two["followers"]:
#     print(f"{person_one["name"]} has {person_one["followers"] - person_two["followers"]} more followers than {person_two["name"]}!")
