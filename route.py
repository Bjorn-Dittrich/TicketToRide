class Route:
    def __init__(self, start: str, end: str, length: int, color: str, score: int):
        """
        Initialize a Route object.

        :param start: The starting city of the route
        :param end: The ending city of the route
        :param length: The length of the route in train pieces
        :param color: The color of the route (e.g., "red", "blue", "wild")
        :param score: The score value of the route
        """
        self.start = start
        self.end = end
        self.length = length
        self.color = color
        self.score = score
        self.claimed_by = None  # Player who claimed the route

    def claim(self, player):
        """
        Claim the route for a player.

        :param player: The player claiming the route
        """
        if self.claimed_by is not None:
            raise ValueError(f"Route from {self.start} to {self.end} is already claimed by {self.claimed_by.name}!")
        self.claimed_by = player

    def __str__(self):
        """
        String representation of the route.
        """
        return f"Route({self.start} -> {self.end}, length={self.length}, color={self.color}, score={self.score})"