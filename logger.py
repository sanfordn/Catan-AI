import os
"""
logger.py
-Logs any move that the players/bots make
"""

def log(player, message):
    f = open("game-log.txt","a")
    if getSize("game-log.txt") > (1000 * 1024):
        deleteContent(f)
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

def prepSettlementsForLog(board,player):
    #for row in range(len(board)):
    #    for vertex in range(len(board[row])):
    #        print(board[row][vertex], end = ", ")
    #print("\n")
    binaryBoard = []
    for row in range(len(board)):
        for vertex in range(len(board[row])):
            if type(board[row][vertex]) == int:
                binaryBoard.append(0)  #open spot
            elif board[row][vertex][0] == player:
                binaryBoard.append(1) #player owns it
            else:
                binaryBoard.append(0) #someone else owns it
    #print(binaryBoard)
    return binaryBoard




def logSettlement(board,move):
    f = open("log-settlements.txt", "a")
    if getSize("game-log.txt") > (1000 * 1024):
        deleteContent(f)
    for i in board:
        tmp = str(i)
        f.write(tmp)
    f.write("|")
    f.write(str(move))
    f.write("\r\n")
    f.close()
