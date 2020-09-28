from improvedSetup import SetupCatan
from improvedBoard import Board()



##THIS IS FOR DEBUGGING TILL I REFACTOR THIS CRAP

#Ask user if they want to print the board

#CREATE BOARD HERE
SetupCatan = SetupCatan(0,0,0,False,Board)
SetupCatan.initializePlayers().initializeDevCards().
    setUpSettlement(SetupCatan.playerList,"first").
    setUpSettlement(SetupCatan.playerList.reverse(),"second").
    handOutResource()