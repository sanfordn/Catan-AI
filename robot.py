from player import Player
from settlementNN import chooseSettlement, chooseRoads

class Robot(Player):
    def __init__(self, name):
        super().__init__(name)

    def botPlaceSettlement(self,board):
        return chooseSettlement(board)

    def botPlaceRoad(self,board,roads):
        vertex1, vertex2 = chooseRoads(board,roads)
        return vertex1, vertex2

    def botPlaceNewSettlement(self, currentBoard):
        print("idk how to place a settlement you honky ass boi")

    def botPlaceCity(self, original, taken, player):
        print("idk how to place a city you honky ass boi")

    def botThrowAway(self):
        print("idk how to throw away my entire life savings you honky ass boi")

    def botStartTurn(self):
        print("idk how to play this game you honky ass boi")

    def chooseToSteal(self, playerList):
        print("idk how to steal anything you honky ass boi")

    def botChooseResource(self):
        print("idk how to make up my mind you honky ass boi")

    def botCommand(self, lc):
        print("idk how to speak you honky ass boi")
