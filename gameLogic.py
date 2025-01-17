from utils import getGameMode, getGameMap, getTotalPlayers, getAIPlayers
from destinationCard import DestinationDeck

def startGame():
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
    