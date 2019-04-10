from player import Player
import random

class Rando(Player):
    def __init__(self, name):
        super().__init__(name)

    def botPlaceSettlement(self,board):
        return random.randint(0,53)

    def botPlaceRoad(self):
        return random.randint(0,53)

    def botPlaceNewSettlement(self, currentBoard):
        choice = random.randint(0,53)
        for row in range(len(currentBoard)):
            for vertex in range(len(currentBoard[row])):
                if currentBoard[row][vertex] != int: #means someones already there
                    choice = random.randint(0,53)
        return str(choice)

    def botPlaceCity(self, original, taken, player):

        #make a loop so it keeps choosing until it gets a city
        choice = random.randint(0,53)
        for row in range(len(original)):
            for vertex in range(len(original[row])):
                if original[row][vertex] == choice:
                    if taken[row][vertex] == player.name+"S":
                        taken[row][vertex] = player.name+"C"
        return choice,taken


    #check to see if the number rolled is already taken
    def botThrowAway(self):
        choices = ['wheat','ore','brick','sheep','wood']
        randchoice = random.randint(0,len(choices)-1)
        action = choices[randchoice]
        return action


    def botStartTurn(self):
        choices = ["-b","-e","-d","-t"]
        randchoice =  random.randint(0,len(choices)-1)
        action = choices[randchoice]
        return action

    def chooseToSteal(self, playerList):
        randchoice = random.randint(0,len(playerList)-1)
        return playerList[randchoice].name

    def botChooseResource(self):
        r = ["wheat","ore","wood","brick","sheep"]
        choice = random.randint(0,4)
        resource = r[choice]
        return resource


    def botCommand(self, lc):
        #in our NN when our roads are out remove the road building, same thing with settlements and dev cards.
         #what last command (lc) does it look to see if the action before was a -b or not
        if lc == "-b": #build command
            buildchoices = ["-c","-s","-r","-d"] #'-d' is for dev card
            if self.settlements < 1:
                buildchoices.remove("-s")
            if self.cities < 1:
                buildchoices.remove("-c")
            if self.roads < 1:
                buildchoices.remove("-r")
            randchoice = random.randint(0,len(buildchoices)-1)
            #buildchoices = ["-s", "-r", "-c"]
            #randchoice = random.randint(0,2)
            action = buildchoices[randchoice]
            return action
        if lc == "-d":
            devChoices = ["-k","-y","-m","-r"] #'-d' is for dev card
            randchoice = random.randint(0,3)
            action = devChoices[randchoice]
            return action
