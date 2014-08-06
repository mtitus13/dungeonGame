__author__ = 'mtitus'

from game import Game
import sys

game = Game()

if 'debug_makeMap' in sys.argv:
    gameMap = game.new_map()

    room1 = gameMap.add_room()
    room2 = gameMap.add_room(room1, 'north')
    room3 = gameMap.add_room(room1, 'east')
    room4 = gameMap.add_room(room1, 'south')
    room5 = gameMap.add_room(room1, 'west')

    gameMap.save_map("testmap.map")
else:
    gameMap = game.load_map("testmap.map")
    room1 = gameMap.rooms[0]

room1.print_desc(True)