import random

def botPlaceSettlement():
    return random.randint(0,53)

def botPlaceRoad():
    return random.randint(0,53)

def botPlaceNewSettlement(currentBoard):
    choice = random.randint(0,53)
    for row in range(len(currentBoard)):
        for vertex in range(len(currentBoard[row])):
            if currentBoard[row][vertex] != int: #means someones already there
                choice = random.randint(0,53)
    return str(choice)

def botPlaceCity(original,taken,player):

    #make a loop so it keeps choosing until it gets a city
    choice = random.randint(0,53)
    for row in range(len(original)):
        for vertex in range(len(original[row])):
            if original[row][vertex] == choice:
                if taken[row][vertex] == player.name+"S":
                    taken[row][vertex] = player.name+"C"
    return choice,taken


#check to see if the number rolled is already taken
def botThrowAway():
    choices = ['wheat','ore','brick','sheep','wood']
    randchoice = random.randint(0,len(choices)-1)
    action = choices[randchoice]
    return action


def botStartTurn():
    choices = ["-b","-e"]
    randchoice =  random.randint(0,1)
    action = choices[randchoice]
    return action

def chooseToSteal(playerList):
    randchoice = random.randint(0,len(playerList)-1)
    return playerList[randchoice].name



def botCommand(lc):
     #what last command (lc) does it look to see if the action before was a -b or not
    if lc == "-b":
        buildchoices = ["-c","-s","-r","-d"] #'-d' is for dev card
        randchoice = random.randint(0,3)
        action = buildchoices[randchoice]
        return action

def rankPlayers(playerList):
    winList = []

    for p in playerList:
        if p.longestRoad == True:
            p.points +=2
        winList.append([p.points, p.name])
    winList.sort()
    winList.reverse()
    return winList

def printVictory(winList,amount):
    if amount == 2:
        print("\t PLAYER " + winList[0][1] + " WINS WITH "      + str(winList[0][0])+ " POINTS.")
        print("\t PLAYER " + winList[1][1] + " TOOK LAST WITH " + str(winList[1][0])+ " POINTS.")
    if amount == 3:
        print("\t PLAYER " + winList[0][1] + " WINS WITH "        + str(winList[0][0])+ " POINTS.")
        print("\t PLAYER " + winList[1][1] + " TOOK SECOND WITH " + str(winList[1][0])+ " POINTS.")
        print("\t PLAYER " + winList[2][1] + " TOOK LAST WITH "   + str(winList[2][0])+ " POINTS.")
    if amount == 4:
        print("\t PLAYER " + winList[0][1] + " WINS WITH "        + str(winList[0][0])+ " POINTS.")
        print("\t PLAYER " + winList[1][1] + " TOOK SECOND WITH " + str(winList[1][0])+ " POINTS.")
        print("\t PLAYER " + winList[2][1] + " TOOK THIRD WITH "  + str(winList[2][0])+ " POINTS.")
        print("\t PLAYER " + winList[3][1] + " TOOK LAST WITH "   + str(winList[3][0])+ " POINTS.")
