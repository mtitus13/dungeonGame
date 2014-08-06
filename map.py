__author__ = 'mtitus'

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
        print self.title + room_id
        print "    " + self.description
        exits = self.exits.keys()
        if len(exits) == 0:
            exits.append('none')

        print "[Exits: " + reduce(lambda exit_string, exit_name: exit_string + ', ' + exit_name, exits, '') + "]"


class Map:
    def __init__(self):
        self.rooms = []

    def add_room(self):
        room = Room()
        self.rooms[room.id] = room.id
        return room
