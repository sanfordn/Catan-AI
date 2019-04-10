"""
catan.py

This file mostly just holds the main function, which enters the game loop. This
is the file that you will run when starting the game.
"""

from setup import *
from board import *
from developmentCardActions import *
from buildFunctions import *
from gameFunctions import *
from tradeFunctions import *
from player import Player
from logger import *

def printHelp():
    '''
    Outputs a list of commands that a user can call during their turn.
    '''

    print("\t-t is for trading, either with a player or with the bank.")
    print("\t-b is for building.")
    print("\t-d is for using a development card.")
    print("\t-e is for ending your turn.")

def tallyUsedDevCards(player):
        #tallies the total number of develpoment cards a player used
        totalDict = {
                "Knight": 0,
                "Year of Plenty": 0,
                "Monopoly": 0,
                "Victory Point": 0,
                "Road Building": 0
            }
        finalString = ""
        tmp = []
        for card in player.usedDevCards:
            totalDict[card] +=1

        totalDict["Victory Point"] += player.devCardDict["Victory Point"]

        for amount in totalDict:
            tmp.append(totalDict[amount])

        knights      = str(tmp[0])+ "  Knights, "
        monopoly     = str(tmp[1])+ "  Year of Plenty, "
        yearOfPlenty = str(tmp[2])+ "  Monopoly, "
        roads        = str(tmp[4])+ "  Road Building. "

        victoryPoints = "They also had " +  str(tmp[3])+ "  points from Victory Point cards."
        if player.largestArmy == False:
            largestArmy = "They DIDN'T HAVE the largest army."
        else:
            largestArmy = "They HAVE the largest army."

        if player.longestRoad == False:
            longestRoad = "They DIDN'T HAVE the longest road."
        else:
            longestRoad = "The HAVE the longest road."



        finalString = "They used " + knights + monopoly + yearOfPlenty + roads + victoryPoints + largestArmy + longestRoad

        return finalString

def rankPlayers(playerList):
        winList = []
        for p in playerList:
            if p.longestRoad == True:
                p.points +=2
            if p.largestArmy == True:
                p.points +=2
            totalDevCards = tallyUsedDevCards(p)
            p.points += p.devCardDict["Victory Point"]
            winList.append([p.points, p.name, totalDevCards])
        winList.sort()
        winList.reverse()
        return winList

def printVictory(winList,amount):
        if amount == 2:
            print("\t PLAYER " + winList[0][1] + " WINS WITH      " + str(winList[0][0])+ " POINTS. " + winList[0][2])
            print("\t PLAYER " + winList[1][1] + " TOOK LAST WITH " + str(winList[1][0])+ "  POINTS. " + winList[1][2])
        if amount == 3:
            print("\t PLAYER " + winList[0][1] + " WINS WITH        " + str(winList[0][0])+ " POINTS. "+ winList[0][2])
            print("\t PLAYER " + winList[1][1] + " TOOK SECOND WITH " + str(winList[1][0])+ "  POINTS. "+ winList[1][2])
            print("\t PLAYER " + winList[2][1] + " TOOK LAST WITH   " + str(winList[2][0])+ "  POINTS. "+ winList[2][2])
        if amount == 4:
            print("\t PLAYER " + winList[0][1] + " WINS WITH        " + str(winList[0][0])+ " POINTS. "+ winList[0][2])
            print("\t PLAYER " + winList[1][1] + " TOOK SECOND WITH " + str(winList[1][0])+ "  POINTS. "+ winList[1][2])
            print("\t PLAYER " + winList[2][1] + " TOOK THIRD WITH  " + str(winList[2][0])+ "  POINTS. "+ winList[2][2])
            print("\t PLAYER " + winList[3][1] + " TOOK LAST WITH   " + str(winList[3][0])+ "  POINTS. "+ winList[3][2])

if __name__ == "__main__":
    playerList = initializePlayers()
    devCardDeck = initializeDevCards()
    board = createBoard()

    # Setup Phase
    placeFirstSettlements(board, playerList)
    exit()

    # Game Phase
    currentPlayerIndex = 0
    #while(not playerList[currentPlayerIndex].victorious()):
    playing = True
    while(playing):
        currentPlayer = playerList[currentPlayerIndex]
        board.printBoard()

        # Roll the dice and resolve consequences of the dice roll
        roll = diceRoll()
        print()
        print("A " + str(roll) + " was rolled.")
        if (roll == 7):
            # Player moves robber
            moveRobber(board, currentPlayer, playerList)

            for player in playerList:
                if player.numResources() > 7:
                   halveHand(player, player.numResources(),board)
        else:
            handOutResources(board, playerList, roll)

        # Begin the action phase for the current player
        if currentPlayer.name in board.humans:
            print("Player " + currentPlayer.name + ":")
        elif currentPlayer.name in board.rando:
            print("Rando " + currentPlayer.name + ":")
        else:
            print("Robot " + currentPlayer.name + ":")
        currentPlayer.printHand()

        # Keep track of what development cards the player obtains in their turn. They can't immediately use them.
        obtainedDevCards = {
            "Knight": 0,
            "Year of Plenty": 0,
            "Monopoly": 0,
            "Road Building": 0,
            "Victory Point": 0
        }
        # Allow commands
        notDone = True
        usedDevCard = False
        while(notDone):
            print()
            print("What would you like to do? Type a command, or -h for a list of commands.")
            if currentPlayer.name in board.robots:   #Robot
                command = currentPlayer.botStartTurn()
                currentPlayer.lastcommand = command
                currentPlayer.move = command
                print("Robot("+currentPlayer.name+") does "+command)
            elif currentPlayer.name in board.rando:  #Rando
                command = currentPlayer.botStartTurn()
                currentPlayer.lastcommand = command
                currentPlayer.move = command
                print("Bot("+currentPlayer.name+") does "+command)
            else:
                command = input()

            if (command == "-h"):
                printHelp()
            elif (command == "-t"):
                print("\tWho would you like to trade with? Enter the player's name or type \"bank\" if you would like to trade with the bank.")
                if currentPlayer.name in board.rando or currentPlayer.name in board.robots:
                    trader = "Bank"
                else:
                    trader = input("\t")
                    trader = trader.capitalize()

                if (trader == currentPlayer.name):
                    print("\tYou can't trade with yourself.")
                elif (trader == "Bank"):
                    # Trade with the bank
                    bankTrade(board, currentPlayer)
                elif (getPlayerFromName(playerList, trader) != None):
                    # Trade with another player
                    playerTrade(currentPlayer, getPlayerFromName(playerList, trader))
                else:
                    print("\tInvalid command.")
            elif (command == "-b"):
                print("\tWhat would you like to build? Type -c for a city, -s for a settlement, -r for a road, or -d for a development card.")
                if currentPlayer.name in board.robots:
                    toBuild = currentPlayer.botCommand(currentPlayer.lastcommand)
                    currentPlayer.lastcommand = ''
                    currentPlayer.move = toBuild
                    print("Rando("+currentPlayer.name+") does "+ toBuild)
                elif currentPlayer.name in board.rando:
                    toBuild = currentPlayer.botCommand(currentPlayer.lastcommand)
                    currentPlayer.lastcommand = ''
                    currentPlayer.move = toBuild
                    print("Bot("+currentPlayer.name+") does "+ toBuild)
                else:
                    toBuild = input("\t")

                if (toBuild == "-c"):
                    if currentPlayer.cities < 1:
                        print("no more cities")
                    else:
                        buildCity(board, currentPlayer)

                elif (toBuild == "-s"):
                    if currentPlayer.settlements < 1:
                        print("no more settlements")
                    else:
                        buildSettlement(board, currentPlayer)
                elif (toBuild == "-r"):
                    if currentPlayer.roads < 1:
                        print("no more roads")
                    else:
                        buildRoad(board, currentPlayer, playerList)
                elif (toBuild == "-d"):
                    result = buildDevCard(currentPlayer, devCardDeck)
                    if (result != None):
                        obtainedDevCards[result] += 1
                else:
                    print("\tInvalid command.")
            elif (command == '-d'):
                if (usedDevCard):
                    print("\tYou may only use 1 development card per turn.")
                else:
                    usedDevCard = True
                    print("\tWhich development card would you like to use? Type -k to use a knight, -y to use Year of Plenty, -m to use monopoly, or -r to use road building.")
                    if currentPlayer.name in board.robots:
                        toUse = currentPlayer.botCommand(currentPlayer.lastcommand)
                        currentPlayer.lastcommand = toUse
                        currentPlayer.move = toUse
                        print("Robot("+currentPlayer.name+") does "+toUse)
                    elif currentPlayer.name in board.rando:
                        toUse = currentPlayer.botCommand(currentPlayer.lastcommand)
                        currentPlayer.lastcommand = toUse
                        currentPlayer.move = toUse
                        print("Bot("+currentPlayer.name+") does "+toUse)
                    else:
                        toUse = input("\t")
                    if (toUse == "-k"):
                        # Ensures they have a knight, and that they didn't just get it this turn.
                        if (currentPlayer.devCardDict["Knight"] - obtainedDevCards["Knight"] - 1 >= 0):
                            useKnight(board, currentPlayer, playerList)
                            currentPlayer.usedDevCards.append("Knight")
                            print(currentPlayer.usedDevCards)
                        else:
                            print("\tYou can't use a knight.")
                    elif (toUse == "-y"):
                        if (currentPlayer.devCardDict["Year of Plenty"] - obtainedDevCards["Year of Plenty"] - 1 >= 0):
                            yearOfPlenty(currentPlayer)
                            currentPlayer.usedDevCards.append("Year of Plenty")
                        else:
                            print("You can't use year of plenty.")
                    elif (toUse == "-m"):
                        if (currentPlayer.devCardDict["Monopoly"] - obtainedDevCards["Monopoly"] - 1 >= 0):
                            monopoly(playerList, currentPlayer)
                            currentPlayer.usedDevCards.append("Monopoly")
                        else:
                            print("You can't use monopoly.")
                    elif (toUse == "-r"):
                        if (currentPlayer.devCardDict["Road Building"] - obtainedDevCards["Road Building"] - 1 >= 0):
                            roadBuilding(board, currentPlayer, playerList)
                            currentPlayer.usedDevCards.append("Road Building")
                        else:
                            print("You can't use road building.")
                    else:
                        print("\tInvalid command.")
                        usedDevCard = False
            elif (command == "-e"):
                usedDevCard = False
                obtainedDevCards["Knight"] = 0
                obtainedDevCards["Year of Plenty"] = 0
                obtainedDevCards["Monopoly"] = 0
                obtainedDevCards["Road Building"] = 0
                obtainedDevCards["Victory Point"] = 0
                notDone = False
            #elif (command == "dev"):
            #    currentPlayer.move = "dev"
            #    currentPlayer.resourceDict["sheep"] = 1
            #    currentPlayer.resourceDict["ore"] = 1
            #    currentPlayer.resourceDict["wheat"] = 1
            else:
                print("Invalid command.")

        if playerList[currentPlayerIndex].victorious():
            playing = False
        # Switch the current player
        if (currentPlayerIndex != len(playerList) - 1):
            currentPlayerIndex += 1
        else:
            currentPlayerIndex = 0

    #Displays the win
    winList = rankPlayers(playerList)
    printVictory(winList,len(playerList))
