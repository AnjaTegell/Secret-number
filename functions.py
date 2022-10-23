import json
import datetime


def players_name():
    return str(input("What is your name?: "))


def get_past_attempts():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list


def score_printout(score_list):
    for score_dict in score_list:
        score_text = (str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        print("Top scores: " + str(score_list))
        return score_text


def play_game(attempts, secret, name, score_list):
    while True:
        guess = int(input("What is our secret number?: "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "players name": str(name),
                               "secret number": secret})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print("Congratualations, we have a winner! The secret number is " + str(secret) + "!")
            print(f"Attempts needed: {attempts}")
            break

        elif guess > secret:
            print("Try a smaller number")
        elif guess < secret:
            print("Try a bigger number")