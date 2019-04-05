from player import Player

class Robot(Player):
    def __init__(self, name):
        super().__init__(name)

    def botPlaceSettlement(self):
        pass

    def botPlaceRoad(self):
        pass

    def botPlaceNewSettlement(self, currentBoard):
        pass

    def botPlaceCity(self, original, taken, player):
        pass

    def botThrowAway(self):
        pass

    def botStartTurn(self):
        pass

    def chooseToSteal(self, playerList):
        pass

    def botChooseResource(self):
        pass

    def botCommand(self, lc):
        pass
