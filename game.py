import random
from colorama import *
playing = True   
playerOneHealth = 100
playerTwoHealth = 100
init()
class playerOne:
    def turnBasic(playerTwoHealth):
        diceOneRoll = random.randint (1,6)
        diceTwoRoll = random.randint (1,20)
        print(Fore.RED + Style.BRIGHT + "You rolled " + str(diceOneRoll) + " and " + str(diceTwoRoll))
        playerTwoHealth -= diceOneRoll + diceTwoRoll
        print(Fore.RED + Style.BRIGHT + "Player two health " + str(playerTwoHealth))
        return playerTwoHealth
    def turnHeal(playerOneHealth):
        diceOneRoll = random.randint (1,16)
        print(Fore.RED + Style.BRIGHT + "You rolled " + str(diceOneRoll))
        playerOneHealth += diceOneRoll
        print(Fore.RED + Style.BRIGHT + "Player one health " + str(playerOneHealth))
        return playerOneHealth    
class playerTwo:
    def turnBasic(playerOneHealth):
        input("Press enter to roll your dice")
        diceOneRoll = random.randint (1,6)
        diceTwoRoll = random.randint (1,20)
        print(Fore.BLUE + Style.BRIGHT + "You rolled " + str(diceOneRoll) + " and " + str(diceTwoRoll))
        playerOneHealth -= diceOneRoll + diceTwoRoll
        print(Fore.BLUE + Style.BRIGHT + "Player one health " + str(playerOneHealth))
        return playerOneHealth

while playing:
    print(Fore.RED + Style.BRIGHT + "Player One's Turn")
    playerOneChoice = input("Press 1 to attack, press 2 to heal")
    if playerOneChoice == str(1):
        playerTwoHealth = playerOne.turnBasic(playerTwoHealth)
    elif playerOneChoice == str(2):
        playerOneHealth = playerOne.turnHeal(playerOneHealth)
    if playerTwoHealth <= 0:
        print(Fore.RED + Style.BRIGHT + "Player One Wins")
        break
    print(Fore.BLUE + "Player Two's Turn")
    playerOneHealth = playerTwo.turnBasic(playerOneHealth)
    if playerOneHealth <= 0:
        print(Fore.BLUE + Style.BRIGHT + "Player Two Wins")
        break
print("GAME OVER")
        
    
        

        

        