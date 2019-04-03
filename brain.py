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
    choices = ["-b","-e","-d","-t"]
    randchoice =  random.randint(0,3)
    action = choices[randchoice]
    return action

def chooseToSteal(playerList):
    randchoice = random.randint(0,len(playerList)-1)
    return playerList[randchoice].name

def botChooseResource():
    r = ["wheat","ore","wood","brick","sheep"]
    choice = random.randint(0,4)
    resource = r[choice]
    return resource


def botCommand(lc):
    #in our NN when our roads are out remove the road building, same thing with settlements and dev cards.
     #what last command (lc) does it look to see if the action before was a -b or not
    if lc == "-b": #build command
        #buildchoices = ["-c","-s","-r","-d"] #'-d' is for dev card
        buildchoices = ["-s","-r"]
        #randchoice = random.randint(0,3)
        randchoice = random.randint(0,1)
        action = buildchoices[randchoice]
        return action
    if lc == "-d":
        devChoices = ["-k","-y","-m","-r"] #'-d' is for dev card
        randchoice = random.randint(0,3)
        action = devChoices[randchoice]
        return action

def tallyUsedDevCards(alist):
    #tallies the total number of develpoment cards a player used
    totalDict = {
            "Knight": 0,
            "Year of Plenty": 0,
            "Monopoly": 0,
            "Victory Point": 0,
            "Road Building": 0
        }
    finalString = ""
    tmp = []
    for card in alist:
        totalDict[card] +=1

    for amount in totalDict:
        tmp.append(totalDict[amount])

    knights      = str(tmp[0])+ "  Knights, "
    monopoly     = str(tmp[1])+ "  Year of Plenty, "
    yearOfPlenty = str(tmp[2])+ "  Monopoly, "
    roads        = str(tmp[4])+ "  Road Building. "
    victoryPoints = "They also had " + str(tmp[3]) + "  points from Victory Point cards."

    finalString = "They used " + knights + monopoly + yearOfPlenty + roads + victoryPoints

    return finalString

def rankPlayers(playerList):
    winList = []
    for p in playerList:
        if p.longestRoad == True:
            p.points +=2
        if p.largestArmy == True:
            p.points +=2
        totalDevCards = tallyUsedDevCards(p.usedDevCards)
        p.points += p.devCardDict["Victory Point"]
        winList.append([p.points, p.name, totalDevCards])
    winList.sort()
    winList.reverse()
    return winList

def printVictory(winList,amount):
    if amount == 2:
        print("\t PLAYER " + winList[0][1] + " WINS WITH      " + str(winList[0][0])+ " POINTS. " + winList[0][2])
        print("\t PLAYER " + winList[1][1] + " TOOK LAST WITH " + str(winList[1][0])+ "  POINTS. " + winList[1][2])
    if amount == 3:
        print("\t PLAYER " + winList[0][1] + " WINS WITH        " + str(winList[0][0])+ " POINTS. "+ winList[0][2])
        print("\t PLAYER " + winList[1][1] + " TOOK SECOND WITH " + str(winList[1][0])+ "  POINTS. "+ winList[1][2])
        print("\t PLAYER " + winList[2][1] + " TOOK LAST WITH   " + str(winList[2][0])+ "  POINTS. "+ winList[2][2])
    if amount == 4:
        print("\t PLAYER " + winList[0][1] + " WINS WITH        " + str(winList[0][0])+ " POINTS. "+ winList[0][2])
        print("\t PLAYER " + winList[1][1] + " TOOK SECOND WITH " + str(winList[1][0])+ "  POINTS. "+ winList[1][2])
        print("\t PLAYER " + winList[2][1] + " TOOK THIRD WITH  " + str(winList[2][0])+ "  POINTS. "+ winList[2][2])
        print("\t PLAYER " + winList[3][1] + " TOOK LAST WITH   " + str(winList[3][0])+ "  POINTS. "+ winList[3][2])
