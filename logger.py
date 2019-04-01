"""
logger.py
-Logs any move that the players/bots make
"""

def log(player):
    f = open("game-log.txt","a")
    name = player.name
    vp = player.points
    long_road = player.longestRoad
    large_army = player.largestArmy
    move = player.move

    f.write("Player:" + str(name) + "|VictoryPoints:" + str(vp) + "|LongestRoad:"
            + str(long_road) + "|LargestArmy:" + str(large_army) +
            "|Move:" + str(move))
    f.write("\r\n")
    f.close()
