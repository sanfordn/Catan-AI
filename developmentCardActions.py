"""
developmentCardActions.py

This file holds the functions that will be used in playing development cards.
"""

from player import Player
from board import *
from gameFunctions import moveRobber
from random import randint
from setup import *


HUMANS = ["A","B","C","D"]
ROBOTS = ["W","X","Y","Z"]


def useKnight(board, player, playerList):
    '''
    Uses the knight, which moves the robber and appends the knight to the
    player's army. Also calculates who currently has the largest army.
    '''

    # Move robber action
    moveRobber(board, player, playerList)

    player.activeKnights += 1
    # Figure out if the current player now has the largest army
    if (player.activeKnights >= 3):
        largestArmy = True
        for i in playerList:
            if (i.name != player.name):
                # If anyone has more knights or the same number of knights,
                # the current player can't have the largest army.
                if (player.activeKnights <= i.activeKnights):
                    largestArmy = False
                    break
        if (largestArmy):
            # Only one can have the largest army, so make it false for all
            # others
            for i in playerList:
                i.largestArmy = False
            player.largestArmy = True


    # Removes the development card from their hand
    player.devCardDict["Knight"] -= 1


def yearOfPlenty(player,printBool):
    '''
    This gives two resources of the player's choice to the player, which is the
    "player" variable.
    '''

    notReceived = True
    while (notReceived):
        if printBool:
            print("\tWhat's the first resource you would like? Please enter the full name of the resource.")
        if player.name in ROBOTS:
            toGet = player.botChooseResource()
            if printBool: 
                print(toGet) #this is feedback for the CLI to show what bot chose
        else:
            toGet = input("\t")
        if (toGet in player.resourceDict):
            player.resourceDict[toGet] += 1
            notReceived = False
        else:
            if printBool:
                print("\tPlease enter a valid resource.")

    notReceived = True
    while (notReceived):
        if printBool:
            print("\tWhat's the second resource you would like? Please enter the full name of the resource.")
        if player.name in ROBOTS:
            toGet = player.botChooseResource()
            if printBool:
                print(toGet)
        else:
            toGet = input("\t")
        if (toGet in player.resourceDict):
            player.resourceDict[toGet] += 1
            notReceived = False
        else:
            if printBool:
                print("\tPlease enter a valid resource.")

    # Removes the development card from their hand
    player.devCardDict["Year of Plenty"] -= 1


def monopoly(playerList, player,printBool):
    '''
    This takes away all of the other player's resource card of the current
    current player's choice.
    '''

    notReceived = True
    while (notReceived):
        if printBool:
            print("\tWhat resource would you like to take? Please enter the full name of the resource.")
        if player.name  in ROBOTS:
            toGet = player.botChooseResource()
            if printBool:
                print(toGet) #this is feedback for the CLI to show what bot chose
        else:
            toGet = input("\t")
        if (toGet in player.resourceDict):
            # Runs through all the players that are NOT the current one
            for i in playerList:
                if (i.name != player.name):
                    # Adds to the current player hand and removes it from the other player's hand
                    player.resourceDict[toGet] += i.resourceDict[toGet]
                    i.resourceDict[toGet] -= i.resourceDict[toGet]
            notReceived = False
        else:
            if printBool:
                print("\tPlease enter a valid resource.")

    # Removes the development card from their hand
    player.devCardDict["Monopoly"] -= 1


def roadBuilding(board, player, playerList):
    '''
    Builds two roads for the player, free of resource cost.
    '''

    # For building two roads.
    for i in range(0, 2):

        vertex1 = 0
        vertex2 = 0

        notPlaced = True
        if player.name in ROBOTS:
            vertex1 = randint(0,53)
            vertex2 = randint(0,53)
            while(board.canPlaceRoad(vertex1,vertex2,player.name)) == False:
                vertex1 = randint(0,53)
                vertex2 = randint(0,53)

            if board.print_bool:
                print("\tEnter the number of the first vertex your road will connect to.")
                print(str(vertex1))
                print("\tEnter the number of the second vertex your road will connect to.")
                print(str(vertex2))
            board.placeRoad(vertex1, vertex2, player, playerList)
            board.printBoard(board.print_bool)
        else:
            while (notPlaced):
                notReceived = True
                while (notReceived):
                    if board.print_bool:
                        print("\tEnter the number of the first vertex your road will connect to.")
                    vertex1 = input("\t")
                    if (not vertex1.isdigit()):
                        if board.print_bool:
                            print("\tInvalid number.")
                    else:
                        vertex1 = int(vertex1)
                        notReceived = False
                        
                notReceived = True
                while (notReceived):
                    if board.print_bool:
                        print("\tEnter the number of the second vertex your road will connect to.")
                    vertex2 = input("\t")
                    if (not vertex2.isdigit()):
                        print("\tInvalid number.")
                    else:
                        vertex2 = int(vertex2)
                        notReceived = False

                if (board.canPlaceRoad(vertex1, vertex2, player.name)):
                    board.placeRoad(vertex1, vertex2, player, playerList)
                    board.printBoard(board.print_bool)
                    notPlaced = False
                else:
                    if board.print_bool:
                        print("\tIllegal road placement.")

    # Removes the development card from their hand
    player.devCardDict["Road Building"] -= 1
