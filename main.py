import random
import json
import datetime
from functions import *


while True:
    current_time = datetime.datetime.now()
    attempts = 0
    score_list = get_past_attempts()
    selection = input("Would you like to A) Play a new game, B) See the best scores, C) Quit?: ")
    if selection == "A" or selection == "a":
        name = players_name()
        print(name)
        secret = random.randint(1, 30)
        print(secret)
        play_game(attempts, secret, name, score_list)
    elif selection == "B" or selection == "b":
        score_printout(score_list)
    else:
        print("Goodbye")
        break


