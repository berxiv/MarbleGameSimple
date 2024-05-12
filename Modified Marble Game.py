import time
import random
import inquirer

ComputerMarbles = 10
PlayerMarbles = 10
ComputerBet = 0
PlayerBet = 0
PlayerGuess = "Even"

IsPlayerEvenOdd = "Even"
IsComputerEvenOdd = "Even"

def NewComputerBet():
    global IsPlayerEvenOdd, IsComputerEvenOdd, PlayerMarbles, PlayerGuess, ComputerBet, ComputerMarbles, PlayerBet
    ComputerBet = random.randint(1, ComputerMarbles)

def DetermineBets():
    global IsPlayerEvenOdd, IsComputerEvenOdd, PlayerMarbles, PlayerGuess, ComputerBet, ComputerMarbles, PlayerBet
    # Calculate how much the player should win and lose
    HowMuchToWinPlayer = min(PlayerBet, ComputerBet)
    HowMuchToLosePlayer = PlayerBet

    # Calculate how much the computer should win and lose
    HowMuchToWinComputer = min(ComputerBet, PlayerBet)
    HowMuchToLoseComputer = ComputerBet

    if ComputerBet % 2 == 0:
        IsComputerEvenOdd = "Even"
    else:
        IsComputerEvenOdd = "Odd"

    if PlayerBet % 2 == 0:
        IsPlayerEvenOdd = "Even"
    else:
        IsPlayerEvenOdd = "Odd"

    if PlayerGuess == "Even" and IsComputerEvenOdd == "Even":
        print("You win! The Computer had " + str(ComputerBet) + " marbles. (Even)")
        PlayerMarbles += HowMuchToWinPlayer
        ComputerMarbles -= HowMuchToLoseComputer
    elif PlayerGuess == "Even" and IsComputerEvenOdd == "Odd":
        print("Oh no, you lost! The Computer had " + str(ComputerBet) + " marbles. (Odd)")
        PlayerMarbles -= HowMuchToLosePlayer
        ComputerMarbles += HowMuchToWinComputer
    elif PlayerGuess == "Odd" and IsComputerEvenOdd == "Even":
        print("Oh no, you lost! The Computer had " + str(ComputerBet) + " marbles. (Even)")
        PlayerMarbles -= HowMuchToLosePlayer
        ComputerMarbles += HowMuchToWinComputer
    elif PlayerGuess == "Odd" and IsComputerEvenOdd == "Odd":
        print("You win! The Computer had " + str(ComputerBet) + " marbles. (Odd)")
        PlayerMarbles += HowMuchToWinPlayer
        ComputerMarbles -= HowMuchToLoseComputer

def IsGameOver():
    global IsPlayerEvenOdd, IsComputerEvenOdd, PlayerMarbles, PlayerGuess, ComputerBet, ComputerMarbles, PlayerBet
    if PlayerMarbles == 0:
        print("Game is over, you lost!")
        return True

    if ComputerMarbles == 0:
        print("Game is over, you won!")
        return True

    return False

def Instructions():
    print("Welcome to my marble game!")
    time.sleep(3)
    print("Let me give you a quick tutorial")
    time.sleep(3)
    print("You and the computer both have 10 marbles at the start, the goal is to have all of the marbles by the end of the game.")
    time.sleep(5)
    print("In each round you guess if the computer has an odd or even amount of marbles, and you bet an amount of marbles.")
    time.sleep(5)
    print("Once you've bet, the computer will say how many marbles it had and if you guessed the amount it had correctly.")
    time.sleep(4)
    print("If you guess right you get the amount of marbles they have if you have at least that amount (so if you bet 3 and you guessed they had even correctly, and they have 4 you get 3 of their marbles)")
    time.sleep(4)
    print("If you guess their 3 correctly and you have 5, you get all 3 of theirs")
    time.sleep(4)
    print("If you guess wrong, you lose marbles")
    time.sleep(3)
    input("Press enter to start...")
    StartGame()

def StartGame():
    global IsPlayerEvenOdd, IsComputerEvenOdd, PlayerMarbles, PlayerGuess, ComputerBet, ComputerMarbles, PlayerBet
    ComputerMarbles = 10
    PlayerMarbles = 10
    ComputerBet = 0
    PlayerBet = 0
    NewRound()

def NewRound():
    global IsPlayerEvenOdd, IsComputerEvenOdd, PlayerMarbles, PlayerGuess, ComputerBet, ComputerMarbles, PlayerBet
    playerguessprompt = [inquirer.List("guessprompt", message=f"How many marbles would you like to bet? (You have {PlayerMarbles} marbles left)", choices=list(range(1, PlayerMarbles + 1)))]
    playerguessevenoddprompy = [inquirer.List("guessevenoddprompt", message="Do you think the computer has an even amount or odd?", choices=["Even", "Odd"])]
    global PlayerBet, PlayerGuess
    NewComputerBet()
    PlayerBet = inquirer.prompt(playerguessprompt)
    PlayerBet = PlayerBet["guessprompt"]
    time.sleep(2)
    PlayerGuess = inquirer.prompt(playerguessevenoddprompy)
    PlayerGuess = PlayerGuess["guessevenoddprompt"]
    time.sleep(2)
    DetermineBets()
    if not IsGameOver():
        NewRound()

#Instructions()
StartGame()