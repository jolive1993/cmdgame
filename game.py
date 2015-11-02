import random
from colorama import *
import getpass
playing = True   
playerOneHealth = 100
playerTwoHealth = 100
init()
class playerOne:
    def turnBasic(playerTwoHealth):
        diceOneRoll = random.randint (1,6)
        diceTwoRoll = random.randint (1,20)
        print(Fore.RED + Style.BRIGHT + "You hit for " + str(diceOneRoll) + " and " + str(diceTwoRoll))
        playerTwoHealth -= diceOneRoll + diceTwoRoll
        print(Fore.RED + Style.BRIGHT + "Player two health " + str(playerTwoHealth))
        return playerTwoHealth
    def turnHeal(playerOneHealth):
        diceOneRoll = random.randint (1,16)
        print(Fore.RED + Style.BRIGHT + "You healed " + str(diceOneRoll))
        playerOneHealth += diceOneRoll
        print(Fore.RED + Style.BRIGHT + "Player one health " + str(playerOneHealth))
        return playerOneHealth    
class playerTwo:
    def turnBasic(playerOneHealth):
        diceOneRoll = random.randint (1,6)
        diceTwoRoll = random.randint (1,20)
        print(Fore.BLUE + Style.BRIGHT + "You hit for " + str(diceOneRoll) + " and " + str(diceTwoRoll))
        playerOneHealth -= diceOneRoll + diceTwoRoll
        print(Fore.BLUE + Style.BRIGHT + "Player one health " + str(playerOneHealth))
        return playerOneHealth
    def turnHeal(playerTwoHealth):
        diceOneRoll = random.randint (1,16)
        print(Fore.BLUE + Style.BRIGHT + "You healed " + str(diceOneRoll))
        playerTwoHealth += diceOneRoll
        print(Fore.BLUE + Style.BRIGHT + "Player two health " + str(playerTwoHealth))
        return playerTwoHealth  

while playing:
    print(Fore.RED + Style.BRIGHT + "Player One's Turn")
    playerOneTurn = True
    while playerOneTurn:
        playerOneChoice = getpass.getpass(prompt="Press 1 to attack, press 2 to heal", stream=None)
        if playerOneChoice == str(1):
            playerTwoHealth = playerOne.turnBasic(playerTwoHealth)
            break
        elif playerOneChoice == str(2):
            playerOneHealth = playerOne.turnHeal(playerOneHealth)
            break
        else:
            print("Not a valid choice")
    if playerTwoHealth <= 0:
        print(Fore.RED + Style.BRIGHT + "Player One Wins")
        break
    print(Fore.BLUE + "Player Two's Turn")
    playerOneTurn = False
    playerTwoTurn = True
    while playerTwoTurn:
        playerTwoChoice = getpass.getpass(prompt="Press 1 to attack, press 2 to heal", stream=None)
        if playerTwoChoice == str(1):
            playerOneHealth = playerTwo.turnBasic(playerOneHealth)
            break
        elif playerTwoChoice == str(2):
            playerTwoHealth = playerTwo.turnHeal(playerTwoHealth)
            break
        else:
            print("Not a valid choice")
    if playerOneHealth <= 0:
        print(Fore.BLUE + Style.BRIGHT + "Player Two Wins")
        break
print("GAME OVER")
        
    
        

        

        