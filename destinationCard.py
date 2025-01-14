class DestinationCard:
    COLORS = ['Red', 'Blue', 'Green', 'Yellow', 'White', 'Black', 'Purple', 'Orange', 'Locomotive', 'Random']

    def __init__(self, color=None):
        if color and color in self.COLORS:
            self.color = color

    def __repr__(self):
        return f"DestinationCard(color={self.color})"