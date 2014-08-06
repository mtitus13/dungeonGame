from map import *
from player import Player

__author__ = 'mtitus'

class Game:
    def __init__(self):
        self.player = Player()
        self.actors = [self.player]
        """
        :type map: Map
        """
        self.map = None

    def new_map(self):
        """
        Creates a map object and sets it as the active map. Also sets the player's location to room 0
        :rtype: Map
        """
        self.map = Map()
        self.player.roomId = 0
        return self.map

    def load_map(self, mapFileName):
        """
        Creates a map and loads it from disk. Sets the player's location to room 0
        :param string mapFileName: File name
        :rtype: Map
        """
        self.new_map()
        self.map = Map.load_map(mapFileName)
        return self.map