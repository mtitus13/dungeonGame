__author__ = 'mtitus'

from termcolor import colored, cprint
import cPickle, os

class Direction:
    directions = ['north', 'east', 'south', 'west']
    opposites = {'north': 'south', 'east': 'west', 'south': 'north', 'west': 'east'}


class Room:
    id_counter = 0

    def __init__(self):
        self.exits = {}
        self.description = ''
        self.title = ''
        self.id = Room.id_counter
        Room.id_counter += 1

    def print_desc(self, editmode=False):
        """
        Prints the room's title, description, and exits. Additional information is displayed in editmode

        editmode info: Room ID
        :param boolean editmode: Adds editmode information
        """
        room_id = ''
        if editmode:
            room_id = " [ID: %d]" % (self.id,)
        cprint(self.title + room_id, 'yellow', attrs=['bold'])

        cprint("    " + self.description, 'blue')

        exits = self.exits.keys()
        if len(exits) == 0:
            exits.append('none')

        cprint("[Exits: " + reduce(lambda exit_string, exit_name: exit_string + ', ' + exit_name, exits) + "]",
               'white', attrs=['bold'])

    def __str__(self):
        myStr = "<Room ID: %d + Exits: " % self.id
        exits = self.exits.keys()
        if len(exits) == 0:
            exits.append('none')
        myStr += reduce(lambda exit_string, exit_name: exit_string + ', ' + exit_name, exits) + ">"
        return myStr


class Map:
    def __init__(self):
        """
        @type self.rooms: dict[int, Room]
        """
        self.rooms = {}
        self.name = ''

    def add_room(self, fromRoom=None, direction=None):
        """
        Creates a new Room and adds it to the room list
        :param Room fromRoom: If set with direction, creates a link linking this room with the newly created room, and a link back.
        :rtype: Room
        """
        room = Room()
        if fromRoom is not None:
            if direction in Direction.directions:
                backDirection = Direction.opposites[direction]
            else:
                backDirection = "exit"

            fromRoom.exits[direction] = room.id
            room.exits[backDirection] = fromRoom.id
        self.rooms[room.id] = room
        return room

    @staticmethod
    def load_map(mapFileName):
        """
        Gets a map from the maps directory
        :param string mapFileName: file name of map to load. must exist as a file under "maps/" under base directory
        :rtype: Map
        """
        """
        @type map: Map
        """
        map = None
        if os.path.exists("maps/" + mapFileName):
            file = open("maps/" + mapFileName, "r")
            map = cPickle.load(file)
        else:
            raise IOError("Map file not in the maps directory: " + mapFileName)

        return map

    def save_map(self, mapFileName):
        """
        Saves the map in a file under the maps/ directory
        :param string mapFileName: file to save as
        """
        file = open("maps/" + mapFileName, "w")
        cPickle.dump(self, file)