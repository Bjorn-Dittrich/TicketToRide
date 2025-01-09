import json
from route import Route

class GameBoard:
    def __init__(self, json_file: str):
        """
        Initialize the GameBoard with routes from a JSON file.

        :param json_file: Path to the JSON file containing route data
        """
        self.routes = []
        self.cities = set()
        self.load_routes(json_file)

    def load_routes(self, json_file: str):
        """
        Load routes from a JSON file and populate the game board.

        :param json_file: Path to the JSON file
        """
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                for route_info in data.get('routes', []):
                    route = Route(
                        start=route_info['start'],
                        end=route_info['end'],
                        length=route_info['length'],
                        color=route_info['color'],
                        score=route_info['score']
                    )
                    self.routes.append(route)
                    self.cities.update([route.start, route.end])
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {json_file} was not found.")
        except KeyError as e:
            raise ValueError(f"Missing required route key: {e}")

    def get_routes(self):
        """
        Get all routes on the game board.

        :return: List of all Route objects
        """
        return self.routes

    def find_routes_by_city(self, city: str):
        """
        Find all routes connected to a specific city.

        :param city: The city to search for
        :return: List of Route objects connected to the city
        """
        return [route for route in self.routes if route.start == city or route.end == city]

    def __str__(self):
        """
        String representation of the game board.
        """
        return f"GameBoard with {len(self.routes)} routes and {len(self.cities)} cities."

# Example JSON file format:
# {
#     "routes": [
#         {"start": "Seattle", "end": "Portland", "length": 1, "color": "gray", "score": 1},
#         {"start": "Portland", "end": "San Francisco", "length": 5, "color": "pink", "score": 10},
#         {"start": "New York", "end": "Boston", "length": 2, "color": "red", "score": 4}
#     ]
# }

# Example usage:
# game_board = GameBoard("routes.json")
# print(game_board)
# for route in game_board.get_routes():
#     print(route)
# print(game_board.find_routes_by_city("Portland"))