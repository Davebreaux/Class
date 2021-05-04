import random #get random generator for computer choice.

#variables to compare for win conditions
choices = ["rock", "paper", "scissors"]
playerScore = 0
computerScore = 0
rounds = int(input('What score would you like to play to?'))



while playerScore < rounds and computerScore < rounds:
    computerChoice = choices[random.randint(0,2)]
    playerChoice = input('rock, paper, or scisors?').lower()

    choiceCheck = True
    while choiceCheck:
        for choice in choices:
            if playerChoice == choice:
                choiceCheck = False
                break
        else:
            playerChoice = input('Choose: rock, paper, or scissors').lower()

    print(f'Computer chose: {computerChoice}')
    print(f'Player Chose: {playerChoice}')

    if computerChoice == playerChoice:
        print('This round is a tie!')
    elif (computerChoice == 'rock' and playerChoice =='scissors') or (computerChoice == 'paper' and playerChoice == 'rock') or (computerChoice == 'scissors' and playerChoice == 'paper'):
        print('Computer wins this round.')
        computerScore += 1
    else:
        print('Player wins this round!')
        playerScore += 1
    print(f'Computer:{computerScore} Player:{playerScore}')


if computerScore > playerScore:
    print('Computer won. Better luck next time.')
else:
    print('You won! Contratulations!')

input('press enter to continue')