"""
setup.py

This file holds several functions that are used in the setup phase of the Catan
game. The setup phase consists of:

    (1) Finding out how many people are playing
    (2) Getting each player to place their first and second settlements before
        the first dice roll occurs.
"""

import random
from random import shuffle
from player import Player
from rando import Rando
from robot import Robot
from board import *
from logger import *

def initializePlayers():
    '''
    Creates all the players and returns the list they are all in.
    '''
    playerList = []

    players = 0
    robots = 0
    randos = 0
    print_bool = True
    
    answer = input("Do you want to print the board?(y/n)")
    while not(answer == "y" or answer == "n"):
        answer = input("Do you want to print the board?(y/n)")
    if answer == "n":
        print_bool = False
    players = input("How many humans are playing? ")
    while not players.isdigit() or (int(players) > 4) or (int(players) < 0):
        print("Please enter a valid number.")
        players = input("How many humans are playing? ")
    

    #assigns a letter to any Players [ABCD]
    if (int(players) >= 1):
        playerList.append(Player("A"))
    if (int(players) >= 2):
        playerList.append(Player("B"))
    if (int(players) >= 3):
        playerList.append(Player("C"))
    if (int(players) >= 4):
        playerList.append(Player("D"))

    availableBots = 4-int(players)

    if availableBots > 0:
        randos = input("How many random bots are playing? You can have up to " + str(availableBots)+ ": ")
        while (not randos.isdigit() or (int(randos) > 4) or (int(randos) < 0) or (int(randos) > availableBots)):
            print("Please enter a valid number less than or equal to " + str(availableBots)+".")
            randos = input("How many random bots are playing? You can have up to " + str(availableBots)+ ": ")

        availableBots = availableBots - int(randos)

    if availableBots > 0:
        robots = input("How many intelligent bots are playing? You can have up to " + str(availableBots)+ ": ")
        while (not robots.isdigit() or (int(robots) > 4) or (int(robots) < 0) or (int(robots) > availableBots)):
            print("Please enter a valid number less than or equal to " + str(availableBots)+".")
            robots = input("How many random bots are playing? You can have up to " + str(availableBots)+ ": ")
        availableBots = availableBots - int(robots)

    #assigns a letter to any Randos [WXYZ]
    if (int(randos) >= 1):
        playerList.append(Rando("W"))
    if (int(randos) >= 2):
        playerList.append(Rando("X"))
    if (int(randos) >= 3):
        playerList.append(Rando("Y"))
    if (int(randos) >= 4):
        playerList.append(Rando("Z"))

    #assigns number to any robots [1234]
    if (int(robots) >= 1):
        playerList.append(Robot("1"))
    if (int(robots) >= 2):
        playerList.append(Robot("2"))
    if (int(robots) >= 3):
        playerList.append(Robot("3"))
    if (int(robots) >= 4):
        playerList.append(Robot("4"))

    return playerList, print_bool

def initializeDevCards():
    '''
    Creates the deck of the development cards. There starts out with 25
    development cards, and cards will never re-enter the deck.
    '''

    devCards = ["Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Year of Plenty", "Year of Plenty", "Monopoly", "Monopoly", "Road Building", "Road Building", "Victory Point", "Victory Point", "Victory Point", "Victory Point", "Victory Point"]
    shuffle(devCards)
    return devCards

def createBoard(printBool):
    '''
    Creates the board, which is the same structure but has randomly generated
    content within.
    '''

    # A board is comprised of vertices and hexes. First we'll make the vertices.
    vertices = []
    for i in range(0, 54):
        vertices.append(Vertex())

    # Add the ports in the appropriate locations
    vertices[1].port = Port(2, "wood")
    vertices[4].port = Port(2, "wood")
    vertices[2].port = Port(3, "none")
    vertices[6].port = Port(3, "none")
    vertices[7].port = Port(2, "brick")
    vertices[11].port = Port(2, "brick")
    vertices[15].port = Port(2, "wheat")
    vertices[20].port = Port(2, "wheat")
    vertices[21].port = Port(3, "none")
    vertices[27].port = Port(3, "none")
    vertices[37].port = Port(2, "ore")
    vertices[42].port = Port(2, "ore")
    vertices[38].port = Port(3, "none")
    vertices[43].port = Port(3, "none")
    vertices[48].port = Port(2, "sheep")
    vertices[52].port = Port(2, "sheep")
    vertices[50].port = Port(3, "none")
    vertices[53].port = Port(3, "none")

    # Now create the hexes. First, shuffle the terrains.
    terrains = ["wheat", "wheat", "wheat", "wheat", "wood", "wood", "wood", "wood", "sheep", "sheep", "sheep", "sheep", "ore", "ore", "ore", "brick", "brick", "brick", "sand"]
    shuffle(terrains)

    # These will be the numbers associated with the hexes. These will always be
    # the same initial order.
    numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    # Assign each terrain a number. The desert will be 0.
    hexesOrdered = []
    sandAssigned = False
    for i in range(0, 19):
        if (terrains[i] == "sand"):
            sandAssigned = True
            hexesOrdered.append(Hex(terrains[i], 0))
        else:
            if (sandAssigned):
                hexesOrdered.append(Hex(terrains[i], numbers[i-1]))
            else:
                hexesOrdered.append(Hex(terrains[i], numbers[i]))

    # The catan numbers spiral around the board, so we'll have to hardcode that
    # spiral format into it.

    # List of possible curl orders
    hexCurlMatrix = [
        [0, 1, 2, 11, 12, 13, 3, 10, 17, 18, 14, 4, 9, 16, 15, 5, 8, 7, 6],
        [11, 0, 1, 10, 12, 13, 2, 9, 17, 18, 14, 3, 8, 16, 15, 4, 7, 6, 5],
        [10, 11, 0, 9, 17, 12, 1, 8, 16, 18, 13, 2, 7, 15, 14, 3, 6, 5, 4],
        [9, 10, 11, 8, 17, 12, 0, 7, 16, 18, 13, 1, 6, 15, 14, 2, 5, 4, 3],
        [8, 9, 10, 7, 16, 17, 11, 6, 15, 18, 12, 0, 5, 14, 13, 1, 4, 3, 2],
        [7, 8, 9, 6, 16, 17, 10, 5, 15, 18, 12, 11, 4, 14, 13, 0, 3, 2, 1],
        [6, 7, 8, 5, 15, 16, 9, 4, 14, 18, 17, 10, 3, 13, 12, 11, 2, 1, 0],
        [5, 6, 7, 4, 15, 16, 8, 3, 14, 18, 17, 9, 2, 13, 12, 10, 1, 0, 11],
        [4, 5, 6, 3, 14, 15, 7, 2, 13, 18, 16, 8, 1, 12, 17, 9, 0, 11, 10],
        [3, 4, 5, 2, 14, 15, 6, 1, 13, 18, 16, 7, 0, 12, 17, 8, 11, 10, 9],
        [2, 3, 4, 1, 13, 14, 5, 0, 12, 18, 15, 6, 11, 17, 16, 7, 10, 9, 8],
        [1, 2, 3, 0, 13, 14, 4, 11, 12, 18, 15, 5, 10, 17, 16, 6, 9, 8, 7]
    ]

    # Choose a random curl and format the board with it
    curlIndex = random.randint(0, 11)
    hexes = []
    for i in hexCurlMatrix[curlIndex]:
        hexes.append(hexesOrdered[i])
    return Board(vertices, hexes,printBool)

def placeFirstSettlements(board, playerList):
    # Determine who goes first: rotation will still be A, B, C, D though
    startIndex = random.randint(0, 3)
    for i in range(0, startIndex):
        playerList.append(playerList[0])
        playerList.pop(0)

    for i in playerList:
        board.printBoard(board.print_bool)

        firstVertex = 0
        notPlaced = True
        while(notPlaced):
            currentBoard = prepSettlementsForLog(board.vertices,i.name)
            if i.name in board.rando or i.name in board.robots:
                toPlace = i.botPlaceSettlement(currentBoard)
                if (board.canPlaceSettlement(toPlace, i.name, True)):
                    # Legal placement
                    board.placeSettlement(toPlace, i)
                    firstVertex = toPlace
                    if i.name in board.rando:
                        start = "Bot("
                    else:
                        start = "Robot("
                    if board.print_bool:
                        print(start+i.name+") places it's first settlement at "+str(toPlace))
                    board.occupySpot(toPlace, i.name) #takes the spot
                    notPlaced = False
            else:
                toPlace = input("Player " + i.name + ", select the vertex where you want to place your first settlement: ")
                if toPlace.isdigit():
                    toPlace = int(toPlace)
                    if (board.canPlaceSettlement(toPlace, i.name, True)):
                        # Legal placement
                        board.placeSettlement(toPlace, i)
                        firstVertex = toPlace
                        notPlaced = False
                        board.occupySpot(toPlace,i.name)
                    else:
                        if board.print_bool:
                            print("Please enter a valid vertex.")
                else:
                    if board.print_bool:
                        print("Please enter a valid vertex.")
        board.printBoard(board.print_bool)

        logSettlement(currentBoard, toPlace,i.name)  #LOGS SETTLEMENTS PLACED
        #building first roads

        notPlaced = True
        while(notPlaced):
            if i.name in board.rando or i.name in board.robots:
                if i.name in board.rando:
                    toPlace = i.botPlaceRoad(None)
                else:
                    #first vertex respresents the Settlement it was at. 
                    #need to check to see what spots are open
                    spots = board.openVertex(firstVertex,i.name)
                    if 1 in spots:
                        #1 means there is a spot open
                        tmp = i.botPlaceRoad(spots)
                        toPlace = board.vertexRelationMatrix[firstVertex][tmp]
                    
                if (board.canPlaceRoad(firstVertex, toPlace, i.name)):
                    openSpots = board.openVertex(firstVertex,i.name)
                    indexOf = board.vertexRelationMatrix[firstVertex].index(toPlace) + 1
                    logRoads(firstVertex,openSpots,indexOf,i.name)

                    board.placeRoad(firstVertex, toPlace, i, playerList)
                    if i.name in board.rando:
                        start = "Bot("
                    else:
                        start = "Robot("
                    if board.print_bool:
                        print(start+i.name+") places a road at " + str(toPlace))
                    notPlaced = False
            else:
                toPlace = input("Your road will start at vertex " + str(firstVertex) + ". Which vertex do you want it to link to? ")
                if toPlace.isdigit():
                    toPlace = int(toPlace)
                    if (board.canPlaceRoad(firstVertex, toPlace, i.name)):
                        # Legal placement
                        board.placeRoad(firstVertex, toPlace, i, playerList)
                        notPlaced = False
                    else:
                        # Non legal placement
                        if board.print_bool:
                            print("Please enter a valid vertex.")
                else:
                    if board.print_bool:
                        print("Please enter a valid vertex.")

    # To find out what initial resouces to the players should receive
    secondSettlements = []

    for i in range(len(playerList)-1, -1, -1):
        board.printBoard(board.print_bool)
        firtVertex = 0
        notPlaced = True
        while(notPlaced):
            currentBoard = prepSettlementsForLog(board.vertices,playerList[i].name)
            if playerList[i].name in board.rando or playerList[i].name in board.robots:
                toPlace = playerList[i].botPlaceSettlement(currentBoard)
                if (board.canPlaceSettlement(toPlace, playerList[i].name, True)):
                    # Legal placement
                    board.placeSettlement(toPlace, playerList[i])
                    firstVertex = toPlace
                    board.occupySpot(toPlace,playerList[i].name)
                    if board.print_bool:
                        print("Bot("+playerList[i].name+") places its second settlement at " + str(toPlace))
                    secondSettlements.append((playerList[i], toPlace))
                    logSettlement(currentBoard, toPlace,playerList[i].name)
                    notPlaced = False

            else:
                toPlace = input("Player " + playerList[i].name + ", select the vertex where you want to place your second settlement: ")
                if toPlace.isdigit():
                    toPlace = int(toPlace)
                    if (board.canPlaceSettlement(toPlace, playerList[i].name, True)):
                        # Legal placement
                        board.placeSettlement(toPlace, playerList[i])
                        firstVertex = toPlace
                        board.occupySpot(toPlace, playerList[i].name)
                        notPlaced = False
                        secondSettlements.append((playerList[i], toPlace))
                    else:
                        # Non legal placement
                        if board.print_bool:
                            print("Please enter a valid vertex.")
                else:
                    if board.print_bool:
                        print("Please enter a valid vertex.")

        board.printBoard(board.print_bool)

        notPlaced = True
        while(notPlaced):
            if playerList[i].name in board.rando or playerList[i].name in board.robots:
                if playerList[i].name in board.rando:
                    toPlace = playerList[i].botPlaceRoad(None)
                    #first vertex respresents the Settlement it was at. 
                    #need to check to see what spots are open
                if playerList[i].name in board.robots:
                    spots = board.openVertex(firstVertex,playerList[i].name)
                    if 1 in spots:
                        #1 means there is a spot open
                        tmp = playerList[i].botPlaceRoad(spots)
                        toPlace = board.vertexRelationMatrix[firstVertex][tmp]
                board.placeRoad(firstVertex, toPlace, playerList[i], playerList)
                if board.print_bool:
                    print("Bot("+playerList[i].name+") places a road at " + str(toPlace))
                notPlaced = False
            else:
                # Get road
                toPlace = input("Your road will start at vertex " + str(firstVertex) + ". Which vertex do you want it to link to? ")
                if toPlace.isdigit():
                    toPlace = int(toPlace)
                    if (board.canPlaceRoad(firstVertex, toPlace, playerList[i].name)):
                        # Legal placement
                        board.placeRoad(firstVertex, toPlace, playerList[i], playerList)
                        notPlaced = False
                    else:
                        # Non legal placement
                        if board.print_bool:
                            print("Please enter a valid vertex.")
                else:
                    if board.print_bool:
                        print("Please enter a valid vertex.")

    # Hand out first resource
    for i in range(0, 19):
        # j represents the vertexs that is next to the hex i
        for j in board.hexRelationMatrix[i]:
            # k represents the tuple of (player, vertex)
            for k in secondSettlements:
                if j == k[1]:
                    # Hand out that resource
                    if (board.hexes[i].resourceType != "sand"):
                        k[0].resourceDict[board.hexes[i].resourceType] += 1
