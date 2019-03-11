import catan
from player import Player
import subprocess
import io

#This runs teh catan game
catan.main()

class RandomBot():
    def __init__(self):
        bot = Player("bot")
