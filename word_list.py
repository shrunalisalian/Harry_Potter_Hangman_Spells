# TO PLAY HARRY POTTER HANGMAN USE SPELLS.TXT FILE

with open('spells.txt', 'r') as file:
    # Read lines and strip any whitespace or newline characters 
    words = [line.strip() for line in file]
# Now word_list contains all the words in the file 
# print(word_list)




# game_type = input("What Hangman game do you want to play: Trivia or Harry Potter Spells: ")
# if game_type == 'Harry Potter':
#     with open('spells.txt', 'r') as file:
#     # Read lines and strip any whitespace or newline characters 
#         words = [line.strip() for line in file]
#     pass
# else:
#     with open('wordlist.10000.txt', 'r') as file:
#     # Read lines and strip any whitespace or newline characters 
#         words = [line.strip() for line in file]