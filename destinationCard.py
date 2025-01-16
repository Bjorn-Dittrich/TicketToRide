import random

class DestinationDeck:
    def __init__(self):
        self.cards = []
        self.colors = ['Red', 'Blue', 'Green', 'Yellow', 'White', 'Black', 'Purple', 'Orange', 'Locomotive']
        self.createShuffledDeck()

    def createShuffledDeck(self):
        for color in self.COLORS[:-1]:  # Exclude 'Locomotive'
            for _ in range(12):
                self.cards.append(DestinationCard(color))
        for _ in range(14):
            self.cards.append(DestinationCard('Locomotive'))
        random.shuffle(self.cards)

    def shuffleDeck(self, discardPile):
        self.cards.extend(discardPile)
        random.shuffle(self.cards)


class DestinationCard:
    COLORS = ['Red', 'Blue', 'Green', 'Yellow', 'White', 'Black', 'Purple', 'Orange', 'Locomotive']

    def __init__(self, color=None):
        if color and color in self.COLORS:
            self.color = color

    def __repr__(self):
        return f"DestinationCard(color={self.color})"