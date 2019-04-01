"""
logger.py
-Logs any move that the players/bots make
"""

f = open("game-log.txt","-rw")

def log(players, move):
    for player in players:
        name = player.name
        vp = player.points
        long_road = player.longestRoad
        large_army = player.largestArmy
        move = player.lastcommand
        f.write("Player:" + name + "|VictoryPoints:" + vp + "|LongestRoad:"
                + string(long_road) + "|LargestArmy:" + large_army +
                "|Move:" + move + '\n')
