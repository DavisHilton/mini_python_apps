#==========================================
# While Loops 
#==========================================
# i = 1
# j = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print("done")

# while j <= 10:
#     print("*" * j)
#     j = j + 1
# print("done")

#===== Guessing Game =====
import math

sercret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guesses_left = guess_limit - guess_count #counts how many guesess left
    guess = int(input(f"The sercret number is between 1- 10. You have {guesses_left} chances to guess the secret number. Please type in your guess. "))
    guess_count += 1      
   
    if guess == sercret_number:
        print("You guessed right!! You Win!!")  
        break    
   
# this else will not get ran until the while statment breaks or condtion is met      
else:
     print("You did not guess the number and you ran out of guesses. Goodbye ") 