from utils import getGameMode, getGameMap, getTotalPlayers, getAIPlayers
from destinationCard import DestinationDeck
from player import Player
from aiPlayer import AIPlayer

def startMenu():
    print("Welcome to Ticket to Ride")
    gameMap = getGameMap()
    gameMode = getGameMode()
    if(gameMode == "AI"):
        print("AI mode selected")
        loadPlayerAIGame(gameMap)

def loadPlayerAIGame(gameMap):
    print("Loading AI game")
    print(gameMap)
    numPlayers = getTotalPlayers('2-3')
    numAIP = getAIPlayers(numPlayers)
    for i in range(numPlayers-numAIP):
        print("Player", i+1)
        player = Player(input("Enter your name: "))
        print(player)
    for i in range(numAIP):
        print("AI Player", i+1)
        player = AIPlayer(str(i+1))
        print(player)
    