import random
from colorama import *
import getpass  
init()
class Player:
    def __init__(self):
        self.health = 100
        self.powerAttackTurns = 3
class Turn:
    def basic(victimHealth):
        diceOneRoll = random.randint (1,6)
        diceTwoRoll = random.randint (1,20)
        print(Fore.RED + Style.BRIGHT + "You hit for " + str(diceOneRoll) + " and " + str(diceTwoRoll))
        victimHealth -= diceOneRoll + diceTwoRoll
        print(Fore.RED + Style.BRIGHT + "Enemy Health " + str(victimHealth))
        return victimHealth
    def heal(selfHealth):
        diceOneRoll = random.randint (1,16)
        print(Fore.GREEN + Style.BRIGHT + "You healed " + str(diceOneRoll))
        selfHealth += diceOneRoll
        print(Fore.GREEN + Style.BRIGHT + "Your Health " + str(selfHealth))
        return selfHealth
    def powerAttack(victimHealth, selfHealth, player):
        diceOneRoll = random.randint (1,10)
        diceTwoRoll = random.randint (0,100)
        if selfHealth < 10:
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
        victimHealth -= diceOneRoll * damageMultiply
        print(Fore.YELLOW + Style.BRIGHT + "You hit for " + str(diceOneRoll) + " with a multiplyer of " + str(damageMultiply))
        print(Fore.YELLOW + Style.BRIGHT + "Enemy Health " + str(victimHealth))
        print(Fore.YELLOW + Style.BRIGHT + "You have " + str(player.powerAttackTurns) + " power attacks remaining")
        return victimHealth
class Game:
    def game(attacker, defender, name):
        print(Fore.RED + Style.BRIGHT + str(name) + " Turn")
        playerOneTurn = True
        while playerOneTurn:
            playerOneChoice = getpass.getpass(prompt="Press 1 to attack, press 2 to heal, press 3 for power attack", stream=None)
            if playerOneChoice == str(1):
                defender.health = Turn.basic(defender.health)
                break
            elif playerOneChoice == str(2):
                attacker.health = Turn.heal(attacker.health)
                break
            elif playerOneChoice == str(3):
                if attacker.powerAttackTurns > 0:
                    attacker.powerAttackTurns -= 1
                    defender.health = Turn.powerAttack(defender.health, attacker.health, attacker)
                    break
                else:
                    print("You are out of power attacks!")
            else:
                print("Not a valid choice")  
playing = True
playerOne = Player()
playerTwo = Player()
while playing:
    Game.game(playerOne, playerTwo, "Player One")
    if playerTwo.health <= 0:
        print(Fore.RED + Style.BRIGHT + "Player One Wins")
        break
    Game.game(playerTwo, playerOne, "Player Two")
    if playerOne.health <= 0:
        print(Fore.BLUE + Style.BRIGHT + "Player Two Wins")
        break
print("GAME OVER")  