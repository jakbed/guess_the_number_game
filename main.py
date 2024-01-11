from assets import logo
import random
print(logo)


def play_again():
    restart_game = input("Do you want to restart? (y/n): ")
    if restart_game == 'y':
        print("\n"*50)
        game()
    return restart_game

def game():
    def play_game(number_of_attemps, computer_number):
            attemps = number_of_attemps
            print(f"You have {attemps} attempts to find the number")

            guessed = False
            def guess():
                player_choice = int(input("Make a guess: "))
                return player_choice

            while attemps > 0 and guessed == False:
                text = guess()
                if text < computer_number:
                    attemps -= 1
                    print(f"Too low. You have {attemps} attemps left")
                elif text > computer_number:
                    attemps -= 1
                    print(f"Too high. You have {attemps} attemps left")
                else:
                    guessed = True
            if attemps == 0:
                print(f"You lose. Coputer number was: {computer_number}\n")
            else:
               print(f"YOU GUESSED THE NUMBER -> {computer_number}\n")
            play_again()

    print("Welcome to the Number Guessing Game!")
    print("Im thinking about the number from 1 to 100. Can you guess the number? :)")
    difficulty = input("Choose a difficulty. Type 'hard' or 'easy': ")
    computer_number = random.randint(1, 100)
    print(f"test: {computer_number}")
    if difficulty == 'hard':
        play_game(5, computer_number)
        
    elif difficulty == 'easy':
        play_game(10, computer_number)

    else:
         game()


game()