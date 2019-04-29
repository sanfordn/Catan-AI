"""
buildFunctions.py

This file supports all of the 'building' functions, the options being cities,
settlements, roads, and development cards. Each function either gives the player
the requested item and takes away their resources, or stops the action if the
player doesn't have the necessary resources.
"""

from board import *
from player import Player
from random import randint
from logger import *
from setup import *

def buildCity(board, player):
    '''
    Asks the player to build a city on top of one of their currently existing
    settlements.
    '''

    # Checks if the player has the resources needed to build a city
    if (player.resourceDict["wheat"] < 2 or player.resourceDict["ore"] < 3):
        if board.print_bool:
            print("\tYou don't have the necessary resources to build a city.")
        return
    settlementVertices = []
    for i in range(0, len(board.vertices)):
        if (board.vertices[i].playerName == player.name and board.vertices[i].city == False):
            # This means there is a settlement on vertex i
            settlementVertices.append(i)

    # Ensures there's a settlement to put the city on
    if (len(settlementVertices) == 0):
        if board.print_bool:
            print("\tYou have no settlements to     put cities on.")
        return

    board.printBoard(board.print_bool)
    if board.print_bool:
        print()
        print("\tWhich settlement would you like to place it on? Pick the settlement number, starting from top left (and starting from 0).")

    if player.name in board.robots or player.name in board.rando:
        settlementNum,board.takenSpots = player.botPlaceCity(board.hexRelationMatrix,board.takenSpots, player)
    else:
        settlementNum = input("\t")
        if (not settlementNum.isdigit()):
            if board.print_bool:
                print("\tInvalid number.")
            return
        settlementNum = int(settlementNum)
    if (settlementNum < 0 or settlementNum >= len(settlementVertices)):
        if board.print_bool:
            print("\tInvalid number.")
        return

    board.vertices[settlementVertices[settlementNum]].city = True
    player.resourceDict["wheat"] -= 2
    player.resourceDict["ore"] -= 3
    player.points += 1
    player.cities -=1
    board.printBoard(board.print_bool)


def buildSettlement(board, player):
    '''
    Asks the player to build a settlement at a vertex and ensures that the move
    is legal.
    '''

    # Checks if the player has the resources needed to build a settlement
    if (player.resourceDict["wheat"] < 1 or player.resourceDict["wood"] < 1 or player.resourceDict["sheep"] < 1 or player.resourceDict["brick"] < 1):
        if board.print_bool:
            print("\tYou don't have the necessary resources to build a settlement.")
        return

    board.printBoard(board.print_bool)
    if board.print_bool:
        print()
        print("\tWhich vertex would you like to place it on? Pick the vertex number, starting from top left (and starting from 0).")
    if player.name in board.robots or player.name in board.rando:
       vertex = player.botPlaceNewSettlement(board.takenSpots)
    else:
        vertex = input("\t")
    if (not vertex.isdigit()):
        if board.print_bool:
            print("\tInvalid number.")
        return
    vertex = int(vertex)

    # Determines if you can place a settlement on the inputted vertex. False
    # means that this isn't the first settlement of the game.
    if (board.canPlaceSettlement(vertex, player.name, False)):
        #Sets up the board for the ability to be logged.
        currentBoard = prepSettlementsForLog(board.vertices,player.name)
        if player.name in board.robots:
            if board.print_bool:
                print("Robot("+player.name+") places a new settlement at "+ str(vertex))
        elif player.name in board.rando:
            if board.print_bool:
                print("Bot("+player.name+") places a new settlement at "+ str(vertex))

        logSettlement(currentBoard,vertex,player.name)
        board.placeSettlement(vertex, player)
        board.printBoard(board.print_bool)
        player.resourceDict["wheat"] -= 1
        player.resourceDict["wood"] -= 1
        player.resourceDict["sheep"] -= 1
        player.resourceDict["brick"] -= 1
    else:
        if board.print_bool:
            print("\tIllegal settlement placement.")


def buildRoad(board, player, playerList):
    '''
    Asks the player to build a road between to vertices and ensures that the
    move is legal.
    '''

    # Checks if the player has the resources needed to build a road
    if (player.resourceDict["wood"] < 1 or player.resourceDict["brick"] < 1):
        if board.print_bool:
            print("\tYou don't have the necessary resources to build a road.")
        return

    # Get the two vertices the road should connect.
    board.printBoard(board.print_bool)
    print()
    if player.name in board.robots or player.name in board.rando:
        vertex1 = randint(0,53)
        vertex2 = randint(0,53)
        tries = 0
        while(board.canPlaceRoad(vertex1,vertex2,player.name) == False and tries < 50):
            vertex1 = randint(0,53)
            vertex2 = randint(0,53)
            tries += 1
        vertex1 = str(vertex1)
        vertex2 = str(vertex2)
        if board.print_bool:
            print("\tEnter the number of the first vertex it will connect to. " +vertex1)
            print("\tEnter the number of the second vertex it will connect to. "+vertex2)
            
    else:
        if board.print_bool:
            print("\tEnter the number of the first vertex it will connect to.")
        vertex1 = input("\t")
        if (not vertex1.isdigit()):
            if board.print_bool:
                print("\tInvalid number.")
            return
    vertex1 = int(vertex1)

    if player.name not in board.robots and player.name not in board.rando:
        if board.print_bool:
            print("\tEnter the number of the second vertex it will connect to.")
        vertex2 = input("\t")
        if (not vertex2.isdigit()):
            if board.print_bool:
                print("\tInvalid number.")
            return
    vertex2 = int(vertex2)

    # Attempt to place it
    if (board.canPlaceRoad(vertex1, vertex2, player.name)):

        openSpots = board.openVertex(vertex1,player.name)
        indexOf = board.vertexRelationMatrix[vertex1].index(vertex2) + 1
        logRoads(vertex1,openSpots,indexOf,player.name)

        board.placeRoad(vertex1, vertex2, player, playerList)
        board.printBoard(board.print_bool)
        player.resourceDict["wood"] -= 1
        player.resourceDict["brick"] -= 1
    else:
        if board.print_bool:
            print("\tIllegal road placement.")

def buildDevCard(player, devCardDeck,printBool):
    '''
    Gives the player a development card off of the deck, and returns the string
    containing the name of the development card. That's for tracking which cards
    were obtained during the current turn (which the player cannot immediately
    use).
    '''

    # Checks if the player has the resources needed to build a road
    if (player.resourceDict["ore"] < 1 or player.resourceDict["sheep"] < 1 or player.resourceDict["wheat"] < 1):
        if printBool:
            print("\tYou don't have the necessary resources to get a development card.")
        return None

    # Ensures there are still development cards
    if (len(devCardDeck) == 0):
        if printBool:
            print("\tNo more development cards remain.")
        return None

    newCard = devCardDeck.pop()
    player.devCardDict[newCard] += 1
    player.resourceDict["ore"] -= 1
    player.resourceDict["sheep"] -= 1
    player.resourceDict["wheat"] -= 1

    print()
    player.printHand(printBool)

    return newCard
