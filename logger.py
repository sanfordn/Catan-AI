import os
"""
logger.py
-Logs any move that the players/bots make
"""

def log(player, message):
    f = open("game-log.txt","a")
    # if getSize("game-log.txt") > (1000 * 1024):
    #     deleteContent(f)
    name = player.name
    vp = player.points
    long_road = player.longestRoad
    large_army = player.largestArmy
    move = player.move

    f.write("Player:" + str(name) + "|VictoryPoints:" + str(vp) + "|LongestRoad:"
            + str(long_road) + "|LargestArmy:" + str(large_army) +
            str(message))
    f.write("\r\n")
    f.close()

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def prepSettlementsForLog(current,player):
    binaryBoard = []
    for vertex in current:
        if vertex.playerName == player:
            binaryBoard.append(1)
        else:
            binaryBoard.append(0)
    return binaryBoard

def prepRoadsForLog(roads,player):
    roadList = []
    for name in roads:
        if roads[name] ==  player + player: #the name
            roadList.append(1)
        else:
            roadList.append(0)
    return roadList


def logRoads(firstVertex,openSpots,chosenSpot,player):
    f = open("rando-log-roads-stage.txt","a")
    if getSize("rando-log-roads-stage.txt") > (1000 * 1024):
        deleteContent(f)
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
    f = open("rando-log-settlements-stage.txt", "a")
    if getSize("rando-log-settlements-stage.txt") > (1000 * 1024):
        deleteContent(f)
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
    #extracts ONLY the winning data from rando, settlements
    #settlements
    writeWinnerData("rando-log-settlements-stage.txt","rando-log-settlements.txt",winner)
    writeWinnerData("rando-log-roads-stage.txt","rando-log-roads.txt",winner)

def writeWinnerData(fin,fout,winner):
        fin = open(fin,"r+")
        lines = fin.readlines()
        fout = open(fout, "a")
        for line in lines:
            if line[0] == winner:
                fout.write(line)
        deleteContent(fin)
        fin.close()
        fout.close()
