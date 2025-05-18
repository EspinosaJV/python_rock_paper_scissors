# rps game introductory function
def main():
    # rps game introductory prompt
    print("Welcome to EspinosaJV's Rock,Paper,Scissors Python application!")
    print("Would you like to play a quick game of Rock Paper Scissors? (Y/N)")
    userChoice = input().lower()

    # rps game user choice input
    if userChoice == 'y':
        rockPaperScissors()
    elif userChoice == 'n':
        print("Alright, thanks for checking this out!")
        exit()
    else:
        print("Please input appropriately.")
        main()

# rps game proper functionality
def rockPaperScissors():
    print("Welcome to Rock, Paper, Scissors!")

if __name__ == '__main__':
    main()

