__author__ = 'mtitus'

from termcolor import colored, cprint
import cPickle

class Direction:
    directions = ['north', 'east', 'south', 'west']
    opposites = {'north': 'south', 'east': 'west', 'south': 'north', 'west': 'east'}


class Room:
    id_counter = 0

    def __init__(self):
        self.exits = {}
        self.description = ''
        self.title = ''
        self.id_counter += 1
        self.id = self.id_counter

    def print_desc(self, editmode=False):
        room_id = ''
        if editmode:
            room_id = " [ID: %d]" % (self.id,)
        cprint(self.title + room_id, 'yellow', attrs=['bold'])

        cprint("    " + self.description, 'blue')

        exits = self.exits.keys()
        if len(exits) == 0:
            exits.append('none')

        cprint("[Exits: " + reduce(lambda exit_string, exit_name: exit_string + ', ' + exit_name, exits, '') + "]",
               'white', attrs=['bold'])


class Map:
    def __init__(self):
        self.rooms = []

    def add_room(self):
        room = Room()
        self.rooms[room.id] = room.id
        return room

    @staticmethod
    def load_map(mapFileName):
        """
        :param mapFileName: string
        :return: Map
        """
        """
        :type map: Map
        """
        map = cPickle.load("maps/" + mapFileName)
        return map

    def save_map(self, mapFileName):
        """
        :param mapFileName: string
        """
        cPickle.dump(self, "maps/" + mapFileName)