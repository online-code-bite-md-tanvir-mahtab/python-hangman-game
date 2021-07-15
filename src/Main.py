#Step 1 
import random
from replit import clear
from hangman_art import stages,logo
from hangman_words import word_list


ran_word = word_list[random.randint(0,len(word_list)-1)]
print(ran_word)
# creating an empty list called fake_list
fake_list = []
#to keep track of the player lives
player_lives = len(ran_word)
# nwo i am going to loop from the 0 to size of theh ran_word
for ran in range(0,len(ran_word)):
  # now i am going to add the dash to the empty list..
  fake_list.append("_")
# now i am going to print them out..
print(fake_list)
# creating new variable that will kepp the result of the game
end_game = False
print(logo)
while not end_game:
  user_word =  input("Enter the guessing word :").lower()
  clear()
  print(user_word)
  if user_word in fake_list:
    print(f"The word you choose : {user_word} is in the list so you will lose a live")
    player_lives -=1
    if player_lives == 0:
      end_game = True
      print("You Lose The game")
  if len(user_word) >1:
    print("too much")
    user_word = input("Enter the guessing word :").lower()
  else:
    print("right choise")
    for words in range(len(ran_word)):
      if user_word == ran_word[words]:
        fake_list[words] = user_word
    # nwo i am going to check if the guess number dosen't match with
    #the random word then we will decrease the lives by one and if the 
    # lives become 0 then the game will end and print the game over message
    if not user_word in ran_word:
      player_lives -=1
    
    if player_lives == 0:
      end_game = True
      print("You Lose")
    print(fake_list)
    

    if not "_" in fake_list:
      end_game = True
      print("You Win")

  print(stages[player_lives])