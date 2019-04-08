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
