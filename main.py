import random # for computer to make a rps choice

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
    # rps instructions prompt
    print("Welcome to Rock, Paper, Scissors!")
    print("We will be doing this in a first-to-3 basis, whoever gets to 3 points between you or the computer,")
    print("will then be determined the victor!")

    # rps player & computer score counters
    playerScore = 0
    computerScore = 0

    # rps list for input validation purposes
    rpsList = ["rock", "paper", "scissors"]

    # rps game functionality loop
    while (playerScore < 3) and (computerScore < 3):
        print("Take your pick: Rock, paper, or scissors?")
        userChoice = input().lower()
        if userChoice not in rpsList:
            print("Please input appropriately.")
            rockPaperScissors()
        computerChoice = random.randint(0, 2)
        finComputerChoice = rpsList[computerChoice]
        print("User Choice is: ", userChoice)
        print("Computer Choice is: ", finComputerChoice)

if __name__ == '__main__':
    main()

