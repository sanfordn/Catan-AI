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
    print(choice)

    return str(choice)

#check to see if the number rolled is already taken

def botPlaceNewRoad(currentRoads):
    pass

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
        buildchoices = ["-c","-s","-r",] #'-d' is for dev card
        randchoice = random.randint(0,2)
        action = buildchoices[randchoice]
        return "-r"


