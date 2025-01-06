class Player:
    def __init__(self, name: str):
        """
        Initialize a player with a name and default attributes.
        
        :param name: The name of the player
        """
        self.name = name                  # Player's name
        self.trains = 45                  # Number of trains available (default for Ticket to Ride)
        self.hand = []                    # Player's hand of cards (list of card objects or strings)
        self.destinations = []            # Destination cards (list of card objects or strings)
        self.score = 0                    # Player's current score
        self.routes = []                  # Routes claimed by the player

    def draw_train_card(self, card):
        """
        Add a train card to the player's hand.
        
        :param card: The card to add to the player's hand
        """
        self.hand.append(card)

    def draw_destination_card(self, card):
        """
        Add a destination card to the player's destinations.
        
        :param card: The destination card to add
        """
        self.destinations.append(card)

    def claim_route(self, route, cost):
        """
        Claim a route on the board and update the player's state.
        
        :param route: The route object or identifier
        :param cost: The number of trains required to claim the route
        """
        if cost > self.trains:
            raise ValueError(f"{self.name} does not have enough trains to claim this route!")
        self.trains -= cost
        self.routes.append(route)
        self.update_score(route)

    def update_score(self, route):
        """
        Update the player's score based on the claimed route.
        
        :param route: The route object or identifier with a score value
        """
        # Assuming `route` has a `score` attribute
        self.score += route.score

    def show_hand(self):
        """
        Display the player's current hand.
        """
        return f"{self.name}'s hand: {', '.join(self.hand)}"

    def __str__(self):
        """
        String representation of the player.
        """
        return f"Player {self.name}: {self.score} points, {self.trains} trains left"
