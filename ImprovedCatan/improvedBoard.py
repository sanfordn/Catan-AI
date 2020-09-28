"""
board.py

This file holds the representation of the board as well as any functions it may
need. It is comprised of the Vertex and Hex classes, which together along some
other structures makes up the Board class.
"""

import copy
from port import Port
from player import Player

class Vertex:
    '''
    This represents a single vertex on the board. Its number is designated by
    its position in the vertices array. Also, docks will always be on the same
    number vertices, so we don't code them in here.
    '''

    def __init__(self):
        self.empty = True
        self.playerName = ''
        self.city = False
        self.port = None


class Hex:
    '''
    This represents a single hex on the board. Its number is designated by its
    position in the hexes array.
    '''

    def __init__(self, resourceType, number):
        self.resourceType = resourceType
        self.number = number
        # Robber always starts on the sand hex.
        if (resourceType == "sand"):
            self.robber = True
        else:
            self.robber = False

    def robberFormat(self):
        if self.robber:
            return "R"
        else:
            return " "

    def debugPrint(self):
        '''
        This should ONLY be used for degbugging purposes. This prints a non
        formatted display of the resource type and number on this hex.
        '''

        print(self.resourceType, self.number)


class Board:
    '''
    This is an object of the entire board.
    '''

    def __init__(self, vertices, hexes,showBoard):
        # List of vertices
        self.vertices = vertices

        # List of hexes
        self.hexes = hexes

        #This makes it so we dont have to see the board
        self.print_bool = showBoard

        # List of humans robots and random robots
        self.humans  = ["A","B","C","D"]
        self.rando   = ["W","X","Y","Z"]
        self.robots  = ["1","2","3","4"]

        # Roads is a dictionary: Key is a tuple of the vertices, value is name
        self.roads = {
            (0, 3): "//",
            (0, 4): "\\\\",
            (1, 4): "//",
            (1, 5): "\\\\",
            (2, 5): "//",
            (2, 6): "\\\\",
            (3, 7): "||",
            (4, 8): "||",
            (5, 9): "||",
            (6, 10): "||",
            (7, 11): "//",
            (7, 12): "\\\\",
            (8, 12): "//",
            (8, 13): "\\\\",
            (9, 13): "//",
            (9, 14): "\\\\",
            (10, 14): "//",
            (10, 15): "\\\\",
            (11, 16): "||",
            (12, 17): "||",
            (13, 18): "||",
            (14, 19): "||",
            (15, 20): "||",
            (16, 21): "//",
            (16, 22): "\\\\",
            (17, 22): "//",
            (17, 23): "\\\\",
            (18, 23): "//",
            (18, 24): "\\\\",
            (19, 24): "//",
            (19, 25): "\\\\",
            (20, 25): "//",
            (20, 26): "\\\\",
            (21, 27): "||",
            (22, 28): "||",
            (23, 29): "||",
            (24, 30): "||",
            (25, 31): "||",
            (26, 32): "||",
            (27, 33): "\\\\",
            (28, 33): "//",
            (28, 34): "\\\\",
            (29, 34): "//",
            (29, 35): "\\\\",
            (30, 35): "//",
            (30, 36): "\\\\",
            (31, 36): "//",
            (31, 37): "\\\\",
            (32, 37): "//",
            (33, 38): "||",
            (34, 39): "||",
            (35, 40): "||",
            (36, 41): "||",
            (37, 42): "||",
            (38, 43): "\\\\",
            (39, 43): "//",
            (39, 44): "\\\\",
            (40, 44): "//",
            (40, 45): "\\\\",
            (41, 45): "//",
            (41, 46): "\\\\",
            (42, 46): "//",
            (43, 47): "||",
            (44, 48): "||",
            (45, 49): "||",
            (46, 50): "||",
            (47, 51): "\\\\",
            (48, 51): "//",
            (48, 52): "\\\\",
            (49, 52): "//",
            (49, 53): "\\\\",
            (50, 53): "//"
        }


        # A matrix that tells what vertices each hex is linked to
        self.hexRelationMatrix = [
            [0, 3, 4, 7, 8, 12],
            [1, 4, 5, 8, 9, 13],
            [2, 5, 6, 9, 10, 14],
            [7, 11, 12, 16, 17, 22],
            [8, 12, 13, 17, 18, 23],
            [9, 13, 14, 18, 19, 24],
            [10, 14, 15, 19, 20, 25],
            [16, 21, 22, 27, 28, 33],
            [17, 22, 23, 28, 29, 34],
            [18, 23, 24, 29, 30, 35],
            [19, 24, 25, 30, 31, 36],
            [20, 25, 26, 31, 32, 37],
            [28, 33, 34, 38, 39, 43],
            [29, 34, 35, 39, 40, 44],
            [30, 35, 36, 40, 41, 45],
            [31, 36, 37, 41, 42, 46],
            [39, 43, 44, 47, 48, 51],
            [40, 44, 45, 48, 49, 52],
            [41, 45, 46, 49, 50, 53]
        ]

        self.takenSpots = [
            [0, 3, 4, 7, 8, 12],
            [1, 4, 5, 8, 9, 13],
            [2, 5, 6, 9, 10, 14],
            [7, 11, 12, 16, 17, 22],
            [8, 12, 13, 17, 18, 23],
            [9, 13, 14, 18, 19, 24],
            [10, 14, 15, 19, 20, 25],
            [16, 21, 22, 27, 28, 33],
            [17, 22, 23, 28, 29, 34],
            [18, 23, 24, 29, 30, 35],
            [19, 24, 25, 30, 31, 36],
            [20, 25, 26, 31, 32, 37],
            [28, 33, 34, 38, 39, 43],
            [29, 34, 35, 39, 40, 44],
            [30, 35, 36, 40, 41, 45],
            [31, 36, 37, 41, 42, 46],
            [39, 43, 44, 47, 48, 51],
            [40, 44, 45, 48, 49, 52],
            [41, 45, 46, 49, 50, 53]
        ]


        # A matrix that tells what vertices each vertex is linked to
        self.vertexRelationMatrix = [
            [3, 4],   #0 is connected to 3,4
            [4, 5],   #1 is connected to 4,5
            [5, 6],   #2 is connected to 5,6
            [0, 7],
            [0, 1, 8],
            [1, 2, 9],
            [2, 10],
            [3, 11, 12],
            [4, 12, 13],
            [5, 13, 14],
            [6, 14, 15],
            [7, 16],
            [7, 8, 17],
            [8, 9, 18],
            [9, 10, 19],
            [10, 20],
            [11, 21, 22],
            [12, 22, 23],
            [13, 23, 24],
            [14, 24, 25],
            [15, 25, 26],
            [16, 27],
            [16, 17, 28],
            [17, 18, 29],
            [18, 19, 30],
            [19, 20, 31],
            [20, 32],
            [21, 33],
            [22, 33, 34],
            [23, 34, 35],
            [24, 35, 36],
            [25, 36, 37],
            [26, 37],
            [27, 28, 38],
            [28, 29, 39],
            [29, 30, 40],
            [30, 31, 41],
            [31, 32, 42],
            [33, 43],
            [34, 43, 44],
            [35, 44, 45],
            [36, 45, 46],
            [37, 46],
            [38, 39, 47],
            [39, 40, 48],
            [40, 41, 49],
            [41, 42, 50],
            [43, 51],
            [44, 51, 52],
            [45, 52, 53],
            [46, 53],
            [47, 48],
            [48, 49],
            [49, 50]
        ]


    def occupySpot(self,piece,player):
        '''
        Goes through the taken spots on the visual representation of the board and replaces the
            chosen vertex with "[PLAYERNAME] + S" to give visual feedback and for logging purposes
        '''
        
        for row in range(len(self.takenSpots)):
            for vertex in range(len(self.takenSpots[row])):
               if self.takenSpots[row][vertex] == piece:
                    self.takenSpots[row][vertex] = player+"S"

    def canPlaceSettlement(self, vertex, playerName, firstPlacement):
        '''
        Determines if a settlement can be placed at the vertex given the user.
        The boolean value firstPlacement determines whether this is the first
        placement, meaning that the game is in the setup phase.
        '''

        # Out of bounds vertex
        if (vertex < 0 or vertex > 53):
            return False

        # Something already there
        if not self.vertices[vertex].empty:
            return False

        # Something at an adjacent vertex
        for i in self.vertexRelationMatrix[vertex]:
            if not self.vertices[i].empty:
                return False

        # Checks if it's connected to a road if it isn't the first placement
        if not firstPlacement:
            for i in self.vertexRelationMatrix[vertex]:
                if (i > vertex):
                    if self.roads[(vertex, i)] == playerName + playerName:
                        return True
                else:
                    if self.roads[(i, vertex)] == playerName + playerName:
                        return True
            return False

        return True


    def placeSettlement(self, vertex, player):
        '''
        Adds a settlement to the board given the vertex and the player's name
        '''

        self.vertices[vertex].empty = False
        self.vertices[vertex].playerName = player.name
        player.points += 1
        player.settlements -= 1

    def canPlaceRoad(self, vertex1, vertex2, playerName):
        '''
        Determines if a road can be placed between the two vertices given the
        user.
        '''
        # Checks if the vertices are next to each other
        if not vertex2 in self.vertexRelationMatrix[vertex1]:
            return False

        #vertex 1 can't be placed if vertex1 is an enemy settlement
        if self.vertices[vertex1].empty == False:
            if (self.vertices[vertex1].playerName != playerName):
                return False


        # Checks if there is already a road there
        if (vertex1 < vertex2):
            if self.roads[(vertex1, vertex2)] == "AA" or self.roads[(vertex1, vertex2)] == "BB" or self.roads[(vertex1, vertex2)] == "CC" or self.roads[(vertex1, vertex2)] == "DD" or \
            self.roads[(vertex1, vertex2)] == "WW" or self.roads[(vertex1, vertex2)] == "XX" or self.roads[(vertex1, vertex2)] == "YY" or self.roads[(vertex1, vertex2)] == "ZZ" or \
            self.roads[(vertex1, vertex2)] == "11" or self.roads[(vertex1, vertex2)] == "22" or self.roads[(vertex1, vertex2)] == "33" or self.roads[(vertex1, vertex2)] == "44":
                return False

        #Bug that fixes above code where if a road was placed at 13 then 8, someone could place a road at 8 then 13, this fixes it.
        if (vertex1 > vertex2):
            if self.roads[(vertex2, vertex1)] == "AA" or self.roads[(vertex2, vertex1)] == "BB" or self.roads[(vertex2, vertex1)] == "CC" or self.roads[(vertex2, vertex1)] == "DD" or \
            self.roads[(vertex2, vertex1)] == "WW" or self.roads[(vertex2, vertex1)] == "XX" or self.roads[(vertex2, vertex1)] == "YY" or self.roads[(vertex2, vertex1)] == "ZZ" or \
            self.roads[(vertex2, vertex1)] == "11" or self.roads[(vertex2, vertex1)] == "22" or self.roads[(vertex2, vertex1)] == "33" or self.roads[(vertex2, vertex1)] == "44":
                return False

        # Checks if there is a settlement of the same playerName at either
        # vertex
        if (not self.vertices[vertex1].empty) and (self.vertices[vertex1].playerName == playerName):
            return True
        if (not self.vertices[vertex2].empty) and (self.vertices[vertex2].playerName == playerName):
            return True

        # Checks if this connects a road already placed
        for i in self.vertexRelationMatrix[vertex1]:
            if (vertex1 < i):
                if self.roads[(vertex1, i)] == playerName + playerName:
                    return True
            else:
                if self.roads[(i, vertex1)] == playerName + playerName:
                    return True
        for i in self.vertexRelationMatrix[vertex2]:
            if (vertex2 < i):
                if self.roads[(vertex2, i)] == playerName + playerName:
                    return True
            else:
                if self.roads[(i, vertex2)] == playerName + playerName:
                    return True

        return False


    def placeRoad(self, vertex1, vertex2, player, playerList):
        '''
        Adds a road to the board given the 2 vertices it is between and the
        player's name
        '''

        if (vertex1 < vertex2):
            self.roads[(vertex1, vertex2)] = player.name + player.name
        else:
            self.roads[(vertex2, vertex1)] = player.name + player.name
        player.roads -=1
        self.assignLongestRoad(player, playerList)
        for i in playerList:
            if self.print_bool:
                print(i.longestRoad)

    def openVertex(self,avertex,player):
        '''
        A vertex is passed in, the function then gets the index of the vertex
            and sees if there are possible road openings.This function returns 
            a 3 digit binary array of open spots, where 1 is open, 0 is closed.
        '''
        openSpots=[]
        for v in self.vertexRelationMatrix[avertex]:
            if self.canPlaceRoad(avertex,v,player):
                openSpots.append(1) #this means its open
            else:
                openSpots.append(0)#means its closed
        if len(openSpots) == 2:
            openSpots.append(0), #means its a port
        return openSpots       
                

    def findRoadEdges(self, playerRoads):
        '''
        Checks to see which road (tuple pair of vertices) is the edge. If there
        is no edge, there must be a cycle, which we will account for later.
        '''

        # The list of edges to be returned
        edges = []

        for road in playerRoads:
            # vertex_ indicates whether that vertex has a connection. If both
            # are True, then this road cannot be an edge.
            vertex1 = False
            vertex2 = False
            # Checks for a connection with the first vertex
            for vertex in self.vertexRelationMatrix[road[0]]:
                if ((road[0], vertex) in playerRoads and (road[0], vertex) != road) or ((vertex, road[0]) in playerRoads and (vertex, road[0]) != road):
                    vertex1 = True

            # Checks for a connection with the second vertex
            for vertex in self.vertexRelationMatrix[road[1]]:
                if ((road[1], vertex) in playerRoads and (road[1], vertex) != road) or ((vertex, road[1]) in playerRoads and (vertex, road[1]) != road):
                    vertex2 = True

            if not (vertex1 and vertex2):
                edges.append(road)

        return edges


    def dfs(self, visited, globalVisited, player, playerRoads, currentRoad, length, used):
        '''
        Runs DFS to find the longest road.
        '''

        visited[currentRoad] = True
        # globalVisited is for ensuring all roads are checked, mainly just
        # applicable for cycles
        globalVisited[currentRoad] = True
        length += 1

        # Because dictionaries are passed by reference in python, we need to do
        # a deepcopy
        visited2 = copy.deepcopy(visited)

        # Detects if you reached the end of the road, in which case check length
        endOfRoad = True

        nextRoad = ()

        nextUsed = -1
        # "used" indicates the vertex it came from. The longest road cannot use
        # this vertex for the next road.
        if (used != 0):
            for vertex in self.vertexRelationMatrix[currentRoad[0]]:
                # Our roads are tracked as (x, y) where x < y, so this figures
                # out the formatting of the road tuple to check
                if (vertex < currentRoad[0]):
                    nextRoad = (vertex, currentRoad[0])
                    nextUsed = 1
                else:
                    nextRoad = (currentRoad[0], vertex)
                    nextUsed = 0

                # This checks if the adjacent road is owned by the player and
                # has not been visited. If so, recurse.
                if nextRoad in playerRoads and visited[nextRoad] == False:
                    self.dfs(visited2, globalVisited, player, playerRoads, nextRoad, length, nextUsed)
                    endOfRoad = False

        if (used != 1):
            for vertex in self.vertexRelationMatrix[currentRoad[1]]:
                # Our roads are tracked as (x, y) where x < y, so this figures
                # out the formatting of the road tuple to check
                if (vertex < currentRoad[1]):
                    nextRoad = (vertex, currentRoad[1])
                    nextUsed = 1
                else:
                    nextRoad = (currentRoad[1], vertex)
                    nextUsed = 0

                if nextRoad in playerRoads and visited[nextRoad] == False:
                    self.dfs(visited2, globalVisited, player, playerRoads, nextRoad, length, nextUsed)
                    endOfRoad = False

        # If you reached the end of the road, check the length to see if it's
        # the longest.
        if endOfRoad and length > player.longestRoadLength:
            player.longestRoadLength = length


    def calculateLongestRoadLength(self, player):
        '''
        Finds the length of the player's longest road, and updates it in
        player.longestRoadLength.
        '''

        playerRoads = {}
        for road in self.roads:
            if (self.roads[road][0] == player.name):
                playerRoads[road] = True

        edges = self.findRoadEdges(playerRoads)

        visited = {}
        globalVisited = {}
        for road in playerRoads:
            visited[road] = False
            globalVisited[road] = False

        for edge in edges:
            self.dfs(visited, globalVisited, player, playerRoads, edge, 0, -1)
            visited = {}
            for road in playerRoads:
                visited[road] = False

        for road in globalVisited:
            if globalVisited[road] == False:
                self.dfs(visited, globalVisited, player, playerRoads, road, 0, 0)


    def assignLongestRoad(self, player, playerList):
        '''
        Calculates who has the longest road.
        '''

        # Player just added a road, so update their longest road length. It may
        # or may not change.
        self.calculateLongestRoadLength(player)

        # Figure out if the current player now has the longest road
        if (player.longestRoadLength >= 5):
            longestRoad = True
            for i in playerList:
                if (i.name != player.name):
                    # If anyone has more roads or the same number of roads, the
                    # current player can't have the longest road.
                    if (player.longestRoadLength <= i.longestRoadLength):
                        longestRoad = False
                        break
            if (longestRoad):
                # Only one can have the largest army, so make it false for all
                # others
                for i in playerList:
                    i.longestRoad = False
                player.longestRoad = True


    def formatHex(self,resource):
        '''
        Helper function for formatting when printing.
        '''

        # Counts extra space if word has an odd length.
        extra_space = 0
        # 18 total spaces between lines in hex
        spaces = 18 - len(str(resource))
        left_space = int(spaces/2)
        right_space = int(spaces/2)
        if spaces%2 == 1:
            extra_space = 1
        return_val = left_space*" " + str(resource) + right_space*" " + extra_space*" "
        return return_val


    def formatVertex(self, index):
        '''
        Helper function for formatting when printing vertices.
        '''
        returnStr = str(index)
        if (self.vertices[index].empty):
            # Returns the formatted number

            if (len(returnStr) == 1):
                return "  0" + returnStr + "  "
            return "  " + returnStr + "  "
        else:
            # Returns the formatted settlement / city
            if (self.vertices[index].city):
                if (len(returnStr) == 1):
                    return self.vertices[index].playerName + "C(0"+returnStr+")"
                return self.vertices[index].playerName + "C(" + returnStr + ")"
            else:
                if (len(returnStr) == 1):
                    return self.vertices[index].playerName + "S(0" + returnStr + ")"
                return self.vertices[index].playerName + "S(" + returnStr + ")"

        #This is one of the more important things to remember. When we look at the board we are going to look
        #at ALL occupied spots and what spots belong to our Brain, using playerNames


    def printBoard(self, printBool):
        if printBool:
            '''
            Prints the board
            '''
            print(" "*10+"                                     Wood                Wildcard")
            print(" "*10+"                            "+self.formatVertex(0)+"   @4,1       "+self.formatVertex(1)+"   @2,6       "+self.formatVertex(2)+"")
            print(" "*10+"                            "+self.roads[(0,3)]+"  "+self.roads[(0,4)]+"              "+self.roads[(1,4)]+"  "+self.roads[(1,5)]+"              "+self.roads[(2,5)]+"  "+self.roads[(2,6)]+"")
            print(" "*10+"                          "+self.roads[(0,3)]+"      "+self.roads[(0,4)]+"          "+self.roads[(1,4)]+"      "+self.roads[(1,5)]+"          "+self.roads[(2,5)]+"      "+self.roads[(2,6)]+"")
            print(" "*10+"                        "+self.roads[(0,3)]+"          "+self.roads[(0,4)]+"      "+self.roads[(1,4)]+"          "+self.roads[(1,5)]+"      "+self.roads[(2,5)]+"          "+self.roads[(2,6)]+"")
            print(" "*10+"                      "+self.roads[(0,3)]+"              "+self.roads[(0,4)]+"  "+self.roads[(1,4)]+"              "+self.roads[(1,5)]+"  "+self.roads[(2,5)]+"              "+self.roads[(2,6)]+" ")
            print(" "*10+"                  "+self.formatVertex(3)+"              "+self.formatVertex(4)+"              "+self.formatVertex(5)+"              "+self.formatVertex(6)+"")
            print(" "*10+"                    "+self.roads[(3,7)]+self.formatHex(self.hexes[0].resourceType)+self.roads[(4,8)]+self.formatHex(self.hexes[1].resourceType)+ self.roads[(5,9)]+self.formatHex(self.hexes[2].resourceType)+ self.roads[(6,10)])
            print(" "*10+"                    "+self.roads[(3,7)]+self.formatHex(self.hexes[0].number)+self.roads[(4,8)]+self.formatHex(self.hexes[1].number)+self.roads[(5,9)]+self.formatHex(self.hexes[2].number)+self.roads[(6,10)])
            print(" "*10+"       Brick        "+self.roads[(3,7)]+"         "+self.hexes[0].robberFormat()+"        "+self.roads[(4,8)]+"         "+self.hexes[1].robberFormat()+"        "+self.roads[(5,9)]+"         "+self.hexes[2].robberFormat()+"        "+self.roads[(6,10)])
            print(" "*10+"       @7,11      "+self.formatVertex(7)+"              "+self.formatVertex(8)+"              "+self.formatVertex(9)+"              "+self.formatVertex(10)+"")
            print(" "*10+"                  "+self.roads[(7,11)]+"  "+self.roads[(7,12)]+"              "+self.roads[(8,12)]+"  "+self.roads[(8,13)]+"              "+self.roads[(9,13)]+"  "+self.roads[(9,14)]+"              "+self.roads[(10,14)]+"  "+self.roads[(10,15)])
            print(" "*10+"                "+self.roads[(7,11)]+"      "+self.roads[(7,12)]+"          "+self.roads[(8,12)]+"      "+self.roads[(8,13)]+"          "+self.roads[(9,13)]+"      "+self.roads[(9,14)]+"          "+self.roads[(10,14)]+"      "+self.roads[(10,15)])
            print(" "*10+"              "+self.roads[(7,11)]+"          "+self.roads[(7,12)]+"      "+self.roads[(8,12)]+"          "+self.roads[(8,13)]+"      "+self.roads[(9,13)]+"          "+self.roads[(9,14)]+"      "+self.roads[(10,14)]+"          "+self.roads[(10,15)])
            print(" "*10+"            "+self.roads[(7,11)]+"              "+self.roads[(7,12)]+"  "+self.roads[(8,12)]+"              "+self.roads[(8,13)]+"  "+self.roads[(9,13)]+"              "+self.roads[(9,14)]+"  "+self.roads[(10,14)]+"              "+self.roads[(10,15)])
            print(" "*10+"        "+self.formatVertex(11)+"              "+self.formatVertex(12)+"              "+self.formatVertex(13)+"              "+self.formatVertex(14)+"              "+self.formatVertex(15)+"")
            print(" "*10+"          "+self.roads[(11,16)]+self.formatHex(self.hexes[3].resourceType)+self.roads[(12,17)]+self.formatHex(self.hexes[4].resourceType)+self.roads[(13,18)]+self.formatHex(self.hexes[5].resourceType)+self.roads[(14,19)]+self.formatHex(self.hexes[6].resourceType)+self.roads[(15,20)]+"       Wheat")
            print(" "*10+"          "+self.roads[(11,16)]+self.formatHex(self.hexes[3].number)+self.roads[(12,17)]+self.formatHex(self.hexes[4].number)+self.roads[(13,18)]+self.formatHex(self.hexes[5].number)+self.roads[(14,19)]+self.formatHex(self.hexes[6].number)+self.roads[(15,20)]+"       @15,20")
            print(" "*10+"          "+self.roads[(11,16)]+"        "+self.hexes[3].robberFormat()+"         "+self.roads[(12,17)]+"       "+self.hexes[4].robberFormat()+"          "+self.roads[(13,18)]+"       "+self.hexes[5].robberFormat()+"          "+self.roads[(14,19)]+"        "+self.hexes[6].robberFormat()+"         "+self.roads[(15,20)])
            print(" "*10+"        "+self.formatVertex(16)+"              "+self.formatVertex(17)+"              "+self.formatVertex(18)+"              "+self.formatVertex(19)+"              "+self.formatVertex(20)+"")
            print(" "*10+"        "+self.roads[(16,21)]+"  "+self.roads[(16,22)]+"               "+self.roads[(17,22)]+"  "+self.roads[(17,23)]+"             "+self.roads[(18,23)]+"  "+self.roads[(18,24)]+"              "+self.roads[(19,24)]+"  "+self.roads[(19,25)]+"              "+self.roads[(20,25)]+"  "+self.roads[(20,26)])
            print(" "*10+"      "+self.roads[(16,21)]+"      "+self.roads[(16,22)]+"           "+self.roads[(17,22)]+"      "+self.roads[(17,23)]+"         "+self.roads[(18,23)]+"      "+self.roads[(18,24)]+"          "+self.roads[(19,24)]+"      "+self.roads[(19,25)]+"          "+self.roads[(20,25)]+"      "+self.roads[(20,26)])
            print(" "*10+"    "+self.roads[(16,21)]+"          "+self.roads[(16,22)]+"      "+self.roads[(17,22)]+"          "+self.roads[(17,23)]+"      "+self.roads[(18,23)]+"          "+self.roads[(18,24)]+"      "+self.roads[(19,24)]+"          "+self.roads[(19,25)]+"      "+self.roads[(20,25)]+"          "+self.roads[(20,26)])
            print(" "*10+"  "+self.roads[(16,21)]+"              "+self.roads[(16,22)]+"  "+self.roads[(17,22)]+"              "+self.roads[(17,23)]+"  "+self.roads[(18,23)]+"              "+self.roads[(18,24)]+"  "+self.roads[(19,24)]+"              "+self.roads[(19,25)]+"  "+self.roads[(20,25)]+"              "+self.roads[(20,26)])
            print("Wildcard"+self.formatVertex(21)+"              "+self.formatVertex(22)+"              "+self.formatVertex(23)+"              "+self.formatVertex(24)+"              "+self.formatVertex(25)+"              "+self.formatVertex(26))
            print("@21,27    "+self.roads[(21,27)]+self.formatHex(self.hexes[7].resourceType)+self.roads[(22,28)]+self.formatHex(self.hexes[8].resourceType)+self.roads[(23,29)]+self.formatHex(self.hexes[9].resourceType)+self.roads[(24,30)]+self.formatHex(self.hexes[10].resourceType)+self.roads[(25,31)]+self.formatHex(self.hexes[11].resourceType)+self.roads[(26,32)])
            print(" "*10+self.roads[(21,27)]+self.formatHex(self.hexes[7].number)+self.roads[(22,28)]+self.formatHex(self.hexes[8].number)+self.roads[(23,29)]+self.formatHex(self.hexes[9].number)+self.roads[(24,30)]+self.formatHex(self.hexes[10].number)+self.roads[(25,31)]+self.formatHex(self.hexes[11].number)+self.roads[(26,32)]+"")
            print(" "*10+self.roads[(21,27)]+"         "+self.hexes[7].robberFormat()+"        "+self.roads[(22,28)]+"        "+self.hexes[8].robberFormat()+"         "+self.roads[(23,29)]+"        "+self.hexes[9].robberFormat()+"         "+self.roads[(24,30)]+"         "+self.hexes[10].robberFormat()+"        "+self.roads[(25,31)]+"         "+self.hexes[11].robberFormat()+"        "+self.roads[(26,32)])
            print(" "*8+self.formatVertex(27)+"              "+self.formatVertex(28)+"              "+self.formatVertex(29)+"              "+self.formatVertex(30)+"              "+self.formatVertex(31)+"              "+self.formatVertex(32))
            print(" "*10+"  "+self.roads[(27,33)]+"              "+self.roads[(28,33)]+"  "+self.roads[(28,34)]+"              "+self.roads[(29,34)]+"  "+self.roads[(29,35)]+"              "+self.roads[(30,35)]+"  "+self.roads[(30,36)]+"              "+self.roads[(31,36)]+"  "+self.roads[(31,37)]+"              "+self.roads[(32,37)])
            print(" "*10+"    "+self.roads[(27,33)]+"          "+self.roads[(28,33)]+"      "+self.roads[(28,34)]+"          "+self.roads[(29,34)]+"      "+self.roads[(29,35)]+"          "+self.roads[(30,35)]+"      "+self.roads[(30,36)]+"          "+self.roads[(31,36)]+"      "+self.roads[(31,37)]+"          "+self.roads[(32,37)])
            print(" "*10+"      "+self.roads[(27,33)]+"      "+self.roads[(28,33)]+"          "+self.roads[(28,34)]+"      "+self.roads[(29,34)]+"          "+self.roads[(29,35)]+"      "+self.roads[(30,35)]+"          "+self.roads[(30,36)]+"      "+self.roads[(31,36)]+"          "+self.roads[(31,37)]+"      "+self.roads[(32,37)])
            print(" "*10+"        "+self.roads[(27,33)]+"  "+self.roads[(28,33)]+"              "+self.roads[(28,34)]+"  "+self.roads[(29,34)]+"              "+self.roads[(29,35)]+"  "+self.roads[(30,35)]+"              "+self.roads[(30,36)]+"  "+self.roads[(31,36)]+"              "+self.roads[(31,37)]+"  "+self.roads[(32,37)])
            print(" "*10+"        "+self.formatVertex(33)+"              "+self.formatVertex(34)+"              "+self.formatVertex(35)+"              "+self.formatVertex(36)+"              "+self.formatVertex(37))
            print(" "*10+"          "+self.roads[(33,38)]+self.formatHex(self.hexes[12].resourceType)+self.roads[(34,39)]+self.formatHex(self.hexes[13].resourceType)+self.roads[(35,40)]+self.formatHex(self.hexes[14].resourceType)+self.roads[(36,41)]+self.formatHex(self.hexes[15].resourceType)+self.roads[(37,42)])
            print(" "*10+"          "+self.roads[(33,38)]+self.formatHex(self.hexes[12].number)+self.roads[(34,39)]+self.formatHex(self.hexes[13].number)+self.roads[(35,40)]+self.formatHex(self.hexes[14].number)+self.roads[(36,41)]+self.formatHex(self.hexes[15].number)+self.roads[(37,42)])
            print(" "*10+"          "+self.roads[(33,38)]+"        "+self.hexes[12].robberFormat()+"         "+self.roads[(34,39)]+"         "+self.hexes[13].robberFormat()+"        "+self.roads[(35,40)]+"        "+self.hexes[14].robberFormat()+"         "+self.roads[(36,41)]+"         "+self.hexes[15].robberFormat()+"        "+self.roads[(37,42)]+"     Ore")
            print(" "*10+"        "+self.formatVertex(38)+"              "+self.formatVertex(39)+"              "+self.formatVertex(40)+"              "+self.formatVertex(41)+"              "+self.formatVertex(42)+"   @37,42")
            print(" "*10+"            "+self.roads[(38,43)]+"              "+self.roads[(39,43)]+"  "+self.roads[(39,44)]+"              "+self.roads[(40,44)]+"  "+self.roads[(40,45)]+"              "+self.roads[(41,45)]+"  "+self.roads[(41,46)]+"              "+self.roads[(42,46)])
            print(" "*10+"              "+self.roads[(38,43)]+"          "+self.roads[(39,43)]+"      "+self.roads[(39,44)]+"          "+self.roads[(40,44)]+"      "+self.roads[(40,45)]+"          "+self.roads[(41,45)]+"      "+self.roads[(41,46)]+"          "+self.roads[(42,46)])
            print(" "*10+"                "+self.roads[(38,43)]+"      "+self.roads[(39,43)]+"          "+self.roads[(39,44)]+"      "+self.roads[(40,44)]+"          "+self.roads[(40,45)]+"      "+self.roads[(41,45)]+"          "+self.roads[(41,46)]+"      "+self.roads[(42,46)])
            print(" "*10+"                  "+self.roads[(38,43)]+"  "+self.roads[(39,43)]+"              "+self.roads[(39,44)]+"  "+self.roads[(40,44)]+"              "+self.roads[(40,45)]+"  "+self.roads[(41,45)]+"              "+self.roads[(41,46)]+"  "+self.roads[(42,46)])
            print(" "*10+"     Wildcard     "+self.formatVertex(43)+"              "+self.formatVertex(44)+"              "+self.formatVertex(45)+"              "+self.formatVertex(46))
            print(" "*10+"     @38,43         "+self.roads[(43,47)]+self.formatHex(self.hexes[16].resourceType)+self.roads[(44,48)]+self.formatHex(self.hexes[17].resourceType)+ self.roads[(45,49)]+self.formatHex(self.hexes[18].resourceType)+ self.roads[(46,50)])
            print(" "*10+"                    "+self.roads[(43,47)]+self.formatHex(self.hexes[16].number)+ self.roads[(44,48)]+self.formatHex(self.hexes[17].number)+ self.roads[(45,49)]+self.formatHex(self.hexes[18].number)+ self.roads[(46,50)])
            print(" "*10+"                    "+self.roads[(43,47)]+"        "+self.hexes[16].robberFormat()+"         "+self.roads[(44,48)]+"         "+self.hexes[17].robberFormat()+"        "+self.roads[(45,49)]+"       "+self.hexes[18].robberFormat()+"          "+self.roads[(46,50)])
            print(" "*10+"                  "+self.formatVertex(47)+"              "+self.formatVertex(48)+"              "+self.formatVertex(49)+"              "+self.formatVertex(50))
            print(" "*10+"                      "+self.roads[(47,51)]+"              "+self.roads[(48,51)]+"  "+self.roads[(48,52)]+"              "+self.roads[(49,52)]+"  "+self.roads[(49,53)]+"              "+self.roads[(50,53)])
            print(" "*10+"                        "+self.roads[(47,51)]+"          "+self.roads[(48,51)]+"      "+self.roads[(48,52)]+"          "+self.roads[(49,52)]+"      "+self.roads[(49,53)]+"          "+self.roads[(50,53)])
            print(" "*10+"                          "+self.roads[(47,51)]+"      "+self.roads[(48,51)]+"          "+self.roads[(48,52)]+"      "+self.roads[(49,52)]+"          "+self.roads[(49,53)]+"      "+self.roads[(50,53)])
            print(" "*10+"                            "+self.roads[(47,51)]+"  "+self.roads[(48,51)]+"              "+self.roads[(48,52)]+"  "+self.roads[(49,52)]+"              "+self.roads[(49,53)]+"  "+self.roads[(50,53)]+"      Wildcard")
            print(" "*10+"                            "+self.formatVertex(51)+"     Sheep    "+self.formatVertex(52)+"              "+self.formatVertex(53)+"      @50,53")
            print(" "*10+"                                       @48,52 ")
        else:
            pass

def createBoard(printBool):
    '''
    Creates the board, which is the same structure but has randomly generated
    content within.
    '''

    # A board is comprised of vertices and hexes. First we'll make the vertices.
    vertices = []
    for i in range(0, 54):
        vertices.append(Vertex())

    # Add the ports in the appropriate locations
    vertices[1].port = Port(2, "wood")
    vertices[4].port = Port(2, "wood")
    vertices[2].port = Port(3, "none")
    vertices[6].port = Port(3, "none")
    vertices[7].port = Port(2, "brick")
    vertices[11].port = Port(2, "brick")
    vertices[15].port = Port(2, "wheat")
    vertices[20].port = Port(2, "wheat")
    vertices[21].port = Port(3, "none")
    vertices[27].port = Port(3, "none")
    vertices[37].port = Port(2, "ore")
    vertices[42].port = Port(2, "ore")
    vertices[38].port = Port(3, "none")
    vertices[43].port = Port(3, "none")
    vertices[48].port = Port(2, "sheep")
    vertices[52].port = Port(2, "sheep")
    vertices[50].port = Port(3, "none")
    vertices[53].port = Port(3, "none")

    # Now create the hexes. First, shuffle the terrains.
    terrains = ["wheat", "wheat", "wheat", "wheat", "wood", "wood", "wood", "wood", "sheep", "sheep", "sheep", "sheep", "ore", "ore", "ore", "brick", "brick", "brick", "sand"]
    shuffle(terrains)

    # These will be the numbers associated with the hexes. These will always be
    # the same initial order.
    numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    # Assign each terrain a number. The desert will be 0.
    hexesOrdered = []
    sandAssigned = False
    for i in range(0, 19):
        if (terrains[i] == "sand"):
            sandAssigned = True
            hexesOrdered.append(Hex(terrains[i], 0))
        else:
            if (sandAssigned):
                hexesOrdered.append(Hex(terrains[i], numbers[i-1]))
            else:
                hexesOrdered.append(Hex(terrains[i], numbers[i]))

    # The catan numbers spiral around the board, so we'll have to hardcode that
    # spiral format into it.

    # List of possible curl orders
    hexCurlMatrix = [
        [0, 1, 2, 11, 12, 13, 3, 10, 17, 18, 14, 4, 9, 16, 15, 5, 8, 7, 6],
        [11, 0, 1, 10, 12, 13, 2, 9, 17, 18, 14, 3, 8, 16, 15, 4, 7, 6, 5],
        [10, 11, 0, 9, 17, 12, 1, 8, 16, 18, 13, 2, 7, 15, 14, 3, 6, 5, 4],
        [9, 10, 11, 8, 17, 12, 0, 7, 16, 18, 13, 1, 6, 15, 14, 2, 5, 4, 3],
        [8, 9, 10, 7, 16, 17, 11, 6, 15, 18, 12, 0, 5, 14, 13, 1, 4, 3, 2],
        [7, 8, 9, 6, 16, 17, 10, 5, 15, 18, 12, 11, 4, 14, 13, 0, 3, 2, 1],
        [6, 7, 8, 5, 15, 16, 9, 4, 14, 18, 17, 10, 3, 13, 12, 11, 2, 1, 0],
        [5, 6, 7, 4, 15, 16, 8, 3, 14, 18, 17, 9, 2, 13, 12, 10, 1, 0, 11],
        [4, 5, 6, 3, 14, 15, 7, 2, 13, 18, 16, 8, 1, 12, 17, 9, 0, 11, 10],
        [3, 4, 5, 2, 14, 15, 6, 1, 13, 18, 16, 7, 0, 12, 17, 8, 11, 10, 9],
        [2, 3, 4, 1, 13, 14, 5, 0, 12, 18, 15, 6, 11, 17, 16, 7, 10, 9, 8],
        [1, 2, 3, 0, 13, 14, 4, 11, 12, 18, 15, 5, 10, 17, 16, 6, 9, 8, 7]
    ]

    # Choose a random curl and format the board with it
    curlIndex = random.randint(0, 11)
    hexes = []
    for i in hexCurlMatrix[curlIndex]:
        hexes.append(hexesOrdered[i])
    return Board(vertices, hexes,printBool)