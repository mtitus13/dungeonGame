__author__ = 'mtitus'

from game import Game
import sys

game = Game()

if 'debug_makeMap' in sys.argv:
    gameMap = game.new_map()

    room1 = gameMap.add_room()
    room1.title = "Center Room"
    room1.description = "This room is the center of a cross. So many directions you can go!"

    room2 = gameMap.add_room(room1, 'north')
    room2.title = "North Dead End"
    room2.description = "The path comes to a dead end here. Better go back to the south."

    room3 = gameMap.add_room(room1, 'east')
    room3.title = "East Dead End"
    room3.description = "There's nowhere else you can go from here."

    room4 = gameMap.add_room(room1, 'south')
    room4.title = "South Dead End"
    room4.description = "The path abruptly ends, leaving you staring at a blank wall. Boring."

    room5 = gameMap.add_room(room1, 'west')
    room5.title = "West Dead End"
    room5.description = "You thought you remembered coming from this direction, but now there's a wall here. Maybe you're misremembering?"

    gameMap.save_map("testmap.map")
else:
    gameMap = game.load_map("testmap.map")
    room1 = gameMap.rooms[0]

gameMap.rooms[game.player.roomId].print_desc()