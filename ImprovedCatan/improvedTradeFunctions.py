"""
tradeFunctions.py

This file supports the two trading functions, which is trading with either
another player or trading with the bank.
"""
from player import *

class SystemTrading():
    def __init__(self):
        self.resourceList  = {
            "wheat": 4,
            "sheep": 4,
            "brick": 4,
            "ore" :  4,
            "wood":  4
            }

    def prepBankTrade(self,player,board):
        #Are there ports
        for vertex in board.vertices:
            #This is a port, but a general wildcard port
            if vertex.playerName == player.name and vertex.port != None:
                #Wildcard
                if vertex.port == 3:
                    for resource in self.resourceList:
                        self.resourceList[resource] = 3
                #Specific Port
                else:
                    for resource in self.resourceList:
                        if (vertex.port.resourceType == resource):
                            self.resourceList[resource] = 2

        print("\t" + str(self.resourceList["wheat"]) + " wheat -> 1 ?")
        print("\t" + str(self.resourceList["sheep"]) + " sheep -> 1 ?")
        print("\t" + str(self.resourceList["brick"]) + " brick -> 1 ?")
        print("\t" + str(self.resourceList["ore"]) + " ore   -> 1 ?")
        print("\t" + str(self.resourceList["wood"]) + " wood  -> 1 ?")

    def tradeBank(self,player):
        tradeIn = input("\t")
        tradeQuantity,tradeMessage = self.checkAvailableTrade(tradeIn,player)
        print(tradeMessage)
        print("\tWhat resource are you trading "+tradeIn+"for?")
        tradeFor = input("\t")
        if tradeFor not in player.resourceDict:
            print("\tInvalid Resource")
        else:
            player.resourceDict[tradeIn] -= tradeQuantity
            player.resourceDict[tradeFor] +=1
        print("\tTrade successfull!")
        player.printHand()


    def checkAvailableTrade(self,resource,player):
        for re in self.resourceList:
            if re == resource:
                if player.resourceDict[resource] < self.resourceList[resource]:
                    return (None, "\tYou dont have enough",resource)
                else:
                    tradeQuantity = self.resourceList[resource]
                    return (tradeQuantity, "\tValid Resource!")
        return (None, "\tInvalid Resource")
        
    def playerTrade(self, playerList):
        p1Quantity, p1Resource = self.prepPlayerTrade(playerList[0])
        p2Quantity, p2Resource = self.prepPlayerTrade(playerList[1])

        #Actual Trade 
        self.prepPlayerTrade(playerList[0]).resourceDict[p1Resource] -= p1Quantity
        self.prepPlayerTrade(playerList[0]).resourceDict[p2Resource] += p2Quantity
        self.prepPlayerTrade(playerList[1]).resourceDict[p1Resource] += p1Quantity
        self.prepPlayerTrade(playerList[1]).resourceDict[p2Resource] -= p2Quantity
        self.prepPlayerTrade(playerList[0]).printHand()

    def prepPlayerTrade(self,player):
        print("\tPlayer " + player.name + ", what resource are you trading in? Type in the full resource name.")
        resource = input("\t")
        if resource not in player.resourceDict:
            print("\tInvalid resource.")
            return

        print("\tHow many " + resource + " are you trading?")
        quantity = input("\t")
        if (not quantity.isdigit()):
            print("\tInvalid number.")
            return
        quantity = int(quantity)
        if (quantity > player.resourceDict[resource] or quantity < 1):
            print("\tYou don't have enough " + resource + ".")
            return
        return quantity, resource