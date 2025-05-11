import random

print("Welcome to the Higher Lower Game!")
print("In this game, you must try to guess which famous person has more followers than the other.")
print("The goal is to get as many correct and accumulate the highest score.")
print("Get one wrong and the game is over...")

user_decision = input("Are you ready to start? Type 'yes' to start or 'q' to quit: ").lower()

people_to_compare = [{"name":"Rihanna", "title": "Musician", "followers": 1000000},{"name":"Beyonce", "title": "Musician", "followers": 2000}, {"name": "GaryVee","title" : "Motivator", "followers": 15990}, {"name":"Donald Trump", "title": "President", "followers": 7000000}, {"name": "Usher", "title":"Musician", "followers": 10000000}, {"name": "Lebron James", "title": "Basketball Player", "followers": 20000000}]

def choose_random_person(list):
    """Randomly chooses and returns a person from the list"""
    new_person = random.choice(list)
    return new_person

person_one = choose_random_person(people_to_compare)
person_two = choose_random_person(people_to_compare)


# if person_one == person_two:
#     person_two = choose_random_person(people_to_compare)
# elif person_one["followers"] > person_two["followers"]:
#     print(f"{person_one["name"]} has {person_one["followers"] - person_two["followers"]} more followers than {person_two["name"]}!")
