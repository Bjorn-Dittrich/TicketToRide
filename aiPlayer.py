class AIPlayer:
    def __init__(self, number):
        """
        Initialize an AI player.

        :param name: The name of the AI player
        :param game_board: The game board object
        """
        self.name = 'AI#' + number
        self.trains = 45  # Default number of trains
        self.hand = []  # Train cards in hand
        self.destinations = []  # Destination cards
        self.routes_claimed = []  # Routes claimed by the AI

    def evaluate_routes(self, board):
        """
        Evaluate all available routes on the board and prioritize them based on score and feasibility.

        :return: A sorted list of routes (highest priority first)
        """
        available_routes = [route for route in self.board.get_routes() if route.claimed_by is None]
        # Example priority: score per train length (score/length)
        prioritized_routes = sorted(available_routes, key=lambda r: r.score / r.length, reverse=True)
        return prioritized_routes

    def make_move(self, board):
        """
        Make a move by selecting the best route to claim or drawing cards.
        """
        prioritized_routes = self.evaluate_routes(board)

        for route in prioritized_routes:
            if route.length <= self.trains:  # Check if enough trains are available
                self.claim_route(route)
                return f"{self.name} claimed the route: {route.start} -> {route.end}"

        # If no routes can be claimed, decide to draw cards (logic not implemented here)
        return f"{self.name} decides to draw cards."

    def claim_route(self, route):
        """
        Claim a route for the AI player.

        :param route: The route to claim
        """
        route.claim(self)
        self.trains -= route.length
        self.routes_claimed.append(route)

    def __str__(self):
        """
        String representation of the AI player.
        """
        return f"AIPlayer {self.name}: {self.trains} trains left, {len(self.routes_claimed)} routes claimed."