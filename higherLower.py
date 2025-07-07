import art
import game_data
import random

print(art.logo)

def select_random_data():
    return random.choice(game_data.data)

answer_check = True
score = 0
team_a = select_random_data()

while answer_check:
    team_b = select_random_data()

    while team_b == team_a:
        team_b = select_random_data()

    if team_a['follower_count'] > team_b['follower_count']:
        answer = "A"
    else:
        answer = "B"

    print(f"Compare A: {team_a['name']}, {team_a['description']}, from {team_a['country']}.")
    print(art.vs)
    print(f"Against B: {team_b['name']}, {team_b['description']}, from {team_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    print("\n" * 30)
    print(art.logo)

    if guess.lower() != answer.lower():
        answer_check = False
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score += 1
        print(f"You're right! Current score: {score}.\n")
        team_a = team_b