import random

def botPlaceSettlement():
    return random.randint(0,53)

def botPlaceRoad():
    return random.randint(0,53)

def botPlaceNewSettlement(currentBoard):
    #BUG: rolls twice then quits doesnt always return a new settlement positions
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
        buildchoices = ["-c","-s","-r","-d"] #'-d' is for dev card
        randchoice = random.randint(0,3)
        #buildchoices = ["-s", "-r", "-c"]
        #randchoice = random.randint(0,2)
        action = buildchoices[randchoice]
        return action
    if lc == "-d":
        devChoices = ["-k","-y","-m","-r"] #'-d' is for dev card
        randchoice = random.randint(0,3)
        action = devChoices[randchoice]
        return action
