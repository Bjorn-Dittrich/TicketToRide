import json

def getGameMode():
    print("Select a game mode:")
    with open('data/availableMaps.json', 'r') as maps_file:
        available_maps = json.load(maps_file)
    print(available_maps)
    for index, map_name in enumerate(available_maps["maps"], start=1):
        print(f"{index}. {map_name["name"]}")
    choice = input("Game mode number: ")
    while(not choice.isdigit() or not (1 <= int(choice) <= len(available_maps["maps"]))):
        print("Invalid game mode number. Please try again.")
        choice = input("Game mode number: ")
    selectedMap = available_maps["maps"][int(choice)-1]
    return loadGameMode(selectedMap)

def loadGameMode(map):
    with open('data/'+map["jsonName"]+'Rules.json', 'r') as rules_file:
        rules = json.load(rules_file)
    with open('data/'+map["jsonName"]+'Map.json', 'r') as map_file:
        game_map = json.load(map_file)
    return {"rules": rules, "map": game_map}