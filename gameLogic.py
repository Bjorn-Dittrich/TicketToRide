from utils import getGameMode, getGameMap
from destinationCard import DestinationDeck

def startGame():
    print("Welcome to Ticket to Ride")
    gameMode = getGameMode()
    gameMap = getGameMap()
    print(gameMode)
    destinationDeck = DestinationDeck()
    print(destinationDeck)
