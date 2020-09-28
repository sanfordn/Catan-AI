"""
setup.py

This file holds several functions that are used in the setup phase of the Catan
game. The setup phase consists of:

    (1) Finding out how many people are playing
    (2) Getting each player to place their first and second settlements before
        the first dice roll occurs.
"""

import random
from improvedPlayer import Player
from improvedRando import Rando

class SetupCatan():
    def __init__(self,players,randos,robots,train,aBoard()):
        self.playerList = []
        self.players = players
        self.randos = randos
        self.robots = robots
        self.availableBots = None
        self.train = train
        self.devCards = None
        self.board = Board()
        self.setUpSettlementResouces = []

    def initializePlayers(self):
        '''
        Creates all the players and returns the list they are all in.
        '''
        #Quick check to see if we are running a training set for our NN. If not then real humans wanna play
        if self.train == False:
            self.players = input("How many humans are playing? ")
            while not self.players.isdigit() or (int(self.players) > 4) or (int(self.players) < 1):
                print("Please enter a valid number.")
                self.players = input("How many humans are playing? ")
            self.players = int(self.players)
            #assigns a letter to any Players [ABCD]
            if self.players >= 1: self.playerList.append(Player("A"))
            if self.players >= 2: self.playerList.append(Player("B"))
            if self.players >= 3: self.playerList.append(Player("C"))
            if self.players >= 4: self.playerList.append(Player("D"))

            self.availableBots = 4-self.players

            if self.availableBots > 0:
                self.randos = input("How many random bots are playing? You can have up to " + str(self.availableBots)+ ": ")
                while (not self.randos.isdigit() or (int(self.randos) > 4) or (int(self.randos) < 0) or (int(self.randos) > self.availableBots)):
                    print("Please enter a valid number less than or equal to " + str(self.availableBots)+".")
                    self.randos = input("How many random bots are playing? You can have up to " + str(self.availableBots)+ ": ")

                self.availableBots -= int(self.randos)

            if self.availableBots > 0:
                self.robots = input("How many intelligent bots are playing? You can have up to " + str(self.availableBots)+ ": ")
                while (not self.robots.isdigit() or (int(self.robots) > 4) or (int(self.robots) < 0) or (int(self.robots) > self.availableBots)):
                    print("Please enter a valid number less than or equal to " + str(self.availableBots)+".")
                    self.robots = input("How many random bots are playing? You can have up to " + str(self.availableBots)+ ": ")
                self.availableBots -= int(self.robots)
            self.randos = int(self.randos)
            self.robots = int(self.robots)
            #assigns a letter to any Randos [WXYZ]
        if self.randos >= 1: self.playerList.append(Rando("W"))
        if self.randos >= 2: self.playerList.append(Rando("X"))
        if self.randos >= 3: self.playerList.append(Rando("Y"))
        if self.randos >= 4: self.playerList.append(Rando("Z"))

        #assigns number to any robots [1234]
        if self.robots >= 1: self.playerList.append(Rando("1"))
        if self.robots >= 2: self.playerList.append(Rando("2"))
        if self.robots >= 3: self.playerList.append(Rando("3"))
        if self.robots >= 4: self.playerList.append(Rando("4"))
        
        self.playerList = random.shuffle(self.playerList)
        return self

    def initializeDevCards(self):
        '''
        Creates the deck of the development cards. There starts out with 25
        development cards, and cards will never re-enter the deck.
        '''

        devCards = ["Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Knight", "Year of Plenty", "Year of Plenty", "Monopoly", "Monopoly", "Road Building", "Road Building", "Victory Point", "Victory Point", "Victory Point", "Victory Point", "Victory Point"]
        random.shuffle(devCards)
        self.devCards = devCards
        return self

    def setUpSettlement(self,playerList,firstOrSecond):

        for i in playerList:
            self.board.printBoard()
            firstVertex = 0
            notPlaced = True
            while(notPlaced):
                if i.name in self.board.rando or i.name in self.board.robots:
                    toPlace = i.botPlaceSettlement()
                    if (self.board.canPlaceSettlement(toPlace, i.name, True)):
                        # Legal placement
                        self.board.placeSettlement(toPlace, i)
                        firstVertex = toPlace
                        if i.name in self.board.rando:
                            start = "Bot("
                        else:
                            start = "Robot("
                        print(start+i.name+") places it's "+firstOrSecond+" settlement at "+str(toPlace))
                        self.board.occupySpot(toPlace, i.name) #takes the spot
                        if firstOrSecond == "second":
                            self.setUpSettlementResouces.append((i,toPlace))

                        notPlaced = False
                else:
                    toPlace = input("Player " + i.name + ", select the vertex where you want to place your "+firstOrSecond+" settlement: ")
                    if toPlace.isdigit():
                        toPlace = int(toPlace)
                        if (self.board.canPlaceSettlement(toPlace, i.name, True)):
                            # Legal placement
                            self.board.placeSettlement(toPlace, i)
                            firstVertex = toPlace
                            notPlaced = False
                            self.board.occupySpot(toPlace,i.name)
                            if firstOrSecond == "second":
                                self.setUpSettlementResouces.append((i,toPlace))
                        else:
                            if self.print_bool:
                                print("Please enter a valid vertex.")
                    else:
                        if self.print_bool:
                            print("Please enter a valid vertex.")
            self.board.printBoard()

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
                            toPlace = board.vertexRelationMatrix[firstVertex][tmp-1]
                        
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
        return self

    def handOutResource(self):
        # Hand out first resource
        for i in range(0, 19):
            # j represents the vertexs that is next to the hex i
            for j in self.board.hexRelationMatrix[i]:
                # k represents the tuple of (player, vertex)
                for k in self.setUpSettlementResouces:
                    if j == k[1]:
                        # Hand out that resource
                        if (self.board.hexes[i].resourceType != "sand"):
                            k[0].resourceDict[board.hexes[i].resourceType] += 1