from player import Player
from settlementNN import chooseSettlement, chooseRoads
import random 

class Robot(Player):
    def __init__(self, name):
        super().__init__(name)

    def botPlaceSettlement(self,board):
        #return chooseSettlement(board)
        aspot = chooseSettlement(board)
        #aspot = random.randint(0,53)
        return aspot

    def botPlaceRoad(self,openSpots):
        avertex = chooseRoads(openSpots)
        return avertex

    def botPlaceNewSettlement(self, currentBoard):
        print("idk how to place a settlement")

    def botPlaceCity(self, original, taken, player):
        print("idk how to place a city")

    def botThrowAway(self):
        print("idk how to throw away my entire life savings")

    def botStartTurn(self):
        print("idk how to play this game")

    def chooseToSteal(self, playerList):
        print("idk how to steal anything")

    def botChooseResource(self):
        print("idk how to make up my mind")

    def botCommand(self, lc):
        print("idk how to speak")
