"""
tradeFunctions.py

This file supports the two trading functions, which is trading with either
another player or trading with the bank.
"""

from board import *
from player import Player

HUMANS = ["A","B","C","D"]
ROBOTS = ["W","X","Y","Z"]

def bankTrade(board, player,printBool):
    '''
    Allows a user to trade with the bank. The player can always do a 4-1
    exchange, but depending on their ports they may be able to do 3-1 or 2-1
    trades as well.
    '''

    if board.print_bool:
        print("\tHere are all possible trades you can do with the bank:")

    wheatReq = 4
    sheepReq = 4
    brickReq = 4
    oreReq = 4
    woodReq = 4

    # Check for ports
    for vertex in board.vertices:
        if vertex.playerName == player.name and vertex.port != None:
            # There is a port
            if vertex.port.number == 3:
                # This is a wild card, so change the default ones
                if wheatReq == 4:
                    wheatReq = 3
                if sheepReq == 4:
                    sheepReq = 3
                if brickReq == 4:
                    brickReq = 3
                if oreReq == 4:
                    oreReq = 3
                if woodReq == 4:
                    woodReq = 3
            else:
                # This is a specific resource port
                if (vertex.port.resourceType == "wheat"):
                    wheatReq = 2
                if (vertex.port.resourceType == "sheep"):
                    sheepReq = 2
                if (vertex.port.resourceType == "brick"):
                    brickReq = 2
                if (vertex.port.resourceType == "ore"):
                    oreReq = 2
                if (vertex.port.resourceType == "wood"):
                    woodReq = 2
    if printBool:
        print("\t" + str(wheatReq) + " wheat -> 1 ?")
        print("\t" + str(sheepReq) + " sheep -> 1 ?")
        print("\t" + str(brickReq) + " brick -> 1 ?")
        print("\t" + str(oreReq) + " ore   -> 1 ?")
        print("\t" + str(woodReq) + " wood  -> 1 ?")

    # Get the resource to be traded in
    if board.print_bool:
        print("\tWhat resource are you trading in? Type in the full resource name.")
    if player.name in ROBOTS:
        tradeIn = player.botChooseResource()
        if board.print_bool:
            print("\t"+tradeIn)
    else:
        tradeIn = input("\t")

    tradeQuantity = 0
    if (tradeIn == "wheat"):
        if player.resourceDict["wheat"] < wheatReq:
            if board.print_bool:
                print("\tYou don't have enough wheat.")
            return
        else:
            tradeQuantity = wheatReq
    elif (tradeIn == "sheep"):
        if player.resourceDict["sheep"] < sheepReq:
            if board.print_bool:
                print("\tYou don't have enough sheep.")
            return
        else:
            tradeQuantity = sheepReq
    elif (tradeIn == "brick"):
        if player.resourceDict["brick"] < brickReq:
            if board.print_bool:
                print("\tYou don't have enough brick.")
            return
        else:
            tradeQuantity = brickReq
    elif (tradeIn == "ore"):
        if player.resourceDict["ore"] < oreReq:
            if board.print_bool:
                print("\tYou don't have enough ore.")
            return
        else:
            tradeQuantity = oreReq
    elif (tradeIn == "wood"):
        if player.resourceDict["wood"] < woodReq:
            if board.print_bool:
                print("\tYou don't have enough wood.")
            return
        else:
            tradeQuantity = woodReq
    else:
        if board.print_bool:
            print("\tInvalid resource.")
        return

    if board.print_bool:
        print("\tWhat resource are you trading " + tradeIn + " for?")
    if player.name in ROBOTS:
        tradeFor = player.botChooseResource()
        if board.print_bool:
            print("\t"+tradeFor)
    else:
        tradeFor = input("\t")
    if not tradeFor in player.resourceDict:
       if board.print_bool:
           print("\tInvalid resource.")
    else:
        # The actual trade itelf
        player.resourceDict[tradeIn] -= tradeQuantity
        player.resourceDict[tradeFor] += 1
        if board.print_bool:
            print("\tTrade successful!")
            print()
        player.printHand(printBool)


def playerTrade(player1, player2):
    '''
    Allows two players to trade with each other. player1 will be the player
    whose turn it currently is.
    '''

    # Get the resource and number to be traded from the first player
    if board.print_bool:
        print("\tPlayer " + player1.name + ", what resource are you trading in? Type in the full resource name.")
    resource1 = input("\t")
    if not resource1 in player1.resourceDict:
        if board.print_bool:
            print("\tInvalid resource.")
        return

    if board.print_bool:
        print("\tHow many " + resource1 + " are you trading?")
    quantity1 = input("\t")
    if (not quantity1.isdigit()):
        if board.print_bool:
            print("\tInvalid number.")
        return
    quantity1 = int(quantity1)
    if (quantity1 > player1.resourceDict[resource1] or quantity1 < 1):
        if board.print_bool:
            print("\tYou don't have enough " + resource1 + ".")
        return

    # Get the resource and number to be traded from the second player
    if board.print_bool:
        print("\tPlayer " + player2.name + ", what resource are you trading in? Type in the full resource name.")
    resource2 = input("\t")
    if not resource2 in player2.resourceDict:
        if board.print_bool:
            print("\tInvalid resource.")
        return

    if board.print_bool:
        print("\tHow many " + resource2 + " are you trading?")
    quantity2 = input("\t")
    if (not quantity2.isdigit()):
        if board.print_bool:
            print("\tInvalid number.")
        return
    quantity2 = int(quantity2)
    if (quantity2 > player2.resourceDict[resource2] or quantity2 < 1):
        if board.print_bool:
            print("\tYou don't have enough " + resource2 + ".")
        return

    # If it reaches this point, the trade has no barriers and can go through
    player1.resourceDict[resource1] -= quantity1
    player1.resourceDict[resource2] += quantity2
    player2.resourceDict[resource1] += quantity1
    player2.resourceDict[resource2] -= quantity2
    if board.print_bool:
        print("\tTrade successful!")
        print()
    player1.printHand()
