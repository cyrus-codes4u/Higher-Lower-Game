#import necessary values
from game_data import data
import art
import random
#Print the logo
print(art.logo)

def select_account():
  return random.choice(data)

def format(account):
  return f"{account['name']}, {account['description']}, from {account['country']}"

def check_answer(guess, person_1, person_2):
  if person_1['follower_count'] > person_2['follower_count']:
    return guess == "a"
  else:
    return guess == "b"

def game():
  person_1 = select_account()
  person_2 = select_account()
  playing = True
  score = 0
  
  while(playing):
    
    if score > 0:
      print(f"Correct! Current score: {score}")
    
    print(f"Compare A: {format(person_1)}")
    print(art.vs)
    print(f"Against B: {format(person_2)}")

    answer = input("Who has more followers, A or B? ").lower()

    if check_answer(answer, person_1, person_2):
      person_1 = person_2
      person_2 = select_account()
      score += 1
    else:
      playing = False
  
  print(f"Sorry, incorrect. Final Score: {score}")

game()
