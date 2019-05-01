import os
"""
logger.py
-Logs any move that the players/bots make
"""

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def prepSettlementsForLog(current,player):
    
    '''
    Creates a list of the settlements on the board and gives a binary representation 
        of all of the settlements
    '''
    
    binaryBoard = []
    for vertex in current:
        if vertex.playerName == player:
            binaryBoard.append(1)
        else:
            binaryBoard.append(0)
    return binaryBoard

def prepRoadsForLog(roads,player):
    
    '''
    Creates a list of the roads on the board and gives a binary representation of all of the 
        roads
    '''
    
    roadList = []
    for name in roads:
        if roads[name] ==  player + player: #the name
            roadList.append(1)
        else:
            roadList.append(0)
    return roadList


def logRoads(firstVertex,openSpots,chosenSpot,player):
    '''
     Logs the playername, the first vertex they chose, a binary array [000] to [111]
            and what spot they chose as a result
     '''
    f = open("logging/rando-log-roads-stage.txt","a")
    f.write(player)
    f.write("|")
    f.write(str(firstVertex))
    f.write("|")
    for i in openSpots:
        tmp = str(i)
        f.write(tmp)
    f.write("|")
    f.write(str(chosenSpot))
    f.write("\r\n")
    f.close()

def logSettlement(board,move,player):
    ''' 
    Logs the settlements they currently own, the settlement they picked, and the player name 
    '''
    f = open("logging/rando-log-settlements-stage.txt", "a")
    f.write(player)
    f.write("|")
    for i in board:
        tmp = str(i)
        f.write(tmp)
    f.write("|")
    f.write(str(move))
    f.write("\r\n")
    f.close()

def getWinnerData(winner):
    '''
    Extracts ONLY the winning data from the staging rando files. for roads and settlements
    '''
    writeWinnerData("logging/rando-log-settlements-stage.txt","logging/rando-log-settlements.txt",winner)
    writeWinnerData("logging/rando-log-roads-stage.txt","logging/rando-log-roads.txt",winner)

def writeWinnerData(fin,fout,winner):
    '''
    Goes through the staging file that is made every game, extracts the winner's data, 
        and then wipes the file
    '''
    fin = open(fin,"r+")
    lines = fin.readlines()
    fout = open(fout, "a")
    for line in lines:
        if line[0] == winner:
            fout.write(line)
    deleteContent(fin)
    fin.close()
    fout.close()
