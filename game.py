import random
from colorama import *
import getpass
playing = True   
playerOneHealth = 100
playerTwoHealth = 100
plPowerAtkTurns = 3
p2PowerAtkTurns = 3
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
    def turnPowerAttack(playerTwoHealth, playerOneHealth):
        diceOneRoll = random.randint (1,10)
        diceTwoRoll = random.randint (0,100)
        if playerOneHealth < 10:
            print(Fore.CYAN + Style.BRIGHT + "Dying mode activated increased chance of damage multiplyer!!!")
            if diceTwoRoll < 30:
                damageMultiply = 2
            elif diceTwoRoll < 60:
                damageMultiply = 3
            else:
                damageMultiply = 5
        else:
            if diceTwoRoll < 60:
                damageMultiply = 2
            elif diceTwoRoll < 90:
                damageMultiply = 3
            else:
                damageMultiply = 4
        playerTwoHealth -= diceOneRoll * damageMultiply
        print(Fore.RED + Style.BRIGHT + "You hit for " + str(diceOneRoll) + " with a multiplyer of " + str(damageMultiply))
        print(Fore.RED + Style.BRIGHT + "Player two health " + str(playerTwoHealth))
        print(Fore.RED + Style.BRIGHT + "You have " + str(plPowerAtkTurns) + " power attacks remaining")
        return playerTwoHealth
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
    def turnPowerAttack(playerOneHealth, playerTwoHealth):
        diceOneRoll = random.randint (1,10)
        diceTwoRoll = random.randint (0,100)
        if playerTwoHealth < 10:
            print(Fore.CYAN + Style.BRIGHT + "Dying mode activated increased chance of damage multiplyer!!!")
            if diceTwoRoll < 30:
                damageMultiply = 2
            elif diceTwoRoll < 60:
                damageMultiply = 3
            else:
                damageMultiply = 5
        else:
            if diceTwoRoll < 60:
                damageMultiply = 2
            elif diceTwoRoll < 90:
                damageMultiply = 3
            else:
                damageMultiply = 4
        playerOneHealth -= diceOneRoll * damageMultiply
        print(Fore.BLUE + Style.BRIGHT + "You hit for " + str(diceOneRoll) + " with a multiplyer of " + str(damageMultiply))
        print(Fore.BLUE + Style.BRIGHT + "Player one health " + str(playerOneHealth))
        print(Fore.BLUE + Style.BRIGHT + "You have " + str(p2PowerAtkTurns) + " power attacks remaining")
        return playerOneHealth
while playing:
    print(Fore.RED + Style.BRIGHT + "Player One's Turn")
    playerOneTurn = True
    while playerOneTurn:
        playerOneChoice = getpass.getpass(prompt="Press 1 to attack, press 2 to heal, press 3 for power attack", stream=None)
        if playerOneChoice == str(1):
            playerTwoHealth = playerOne.turnBasic(playerTwoHealth)
            break
        elif playerOneChoice == str(2):
            playerOneHealth = playerOne.turnHeal(playerOneHealth)
            break
        elif playerOneChoice == str(3):
            if plPowerAtkTurns > 0:
                playerTwoHealth = playerOne.turnPowerAttack(playerTwoHealth, playerOneHealth)
                plPowerAtkTurns -= 1
                break
            else:
                print("You are out of power attacks!")
        else:
            print("Not a valid choice")
    if playerTwoHealth <= 0:
        print(Fore.RED + Style.BRIGHT + "Player One Wins")
        break
    print(Fore.BLUE + "Player Two's Turn")
    playerOneTurn = False
    playerTwoTurn = True
    while playerTwoTurn:
        playerTwoChoice = getpass.getpass(prompt="Press 1 to attack, press 2 to heal, press 3 for power attack", stream=None)
        if playerTwoChoice == str(1):
            playerOneHealth = playerTwo.turnBasic(playerOneHealth)
            break
        elif playerTwoChoice == str(2):
            playerTwoHealth = playerTwo.turnHeal(playerTwoHealth)
            break
        elif playerTwoChoice == str(3):
            if p2PowerAtkTurns > 0:
                playerOneHealth = playerTwo.turnPowerAttack(playerOneHealth, playerTwoHealth)
                p2PowerAtkTurns -= 1
                break
            else:
                print("You are out of power attacks!")
        else:
            print("Not a valid choice")
    if playerOneHealth <= 0:
        print(Fore.BLUE + Style.BRIGHT + "Player Two Wins")
        break
print("GAME OVER")
        
    
        

        

        