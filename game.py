from termcolor import cprint
from map import *
from player import Player
import os

__author__ = 'mtitus'


class Game:
    def __init__(self):
        self.player = Player()
        self.actors = [self.player]
        self.playing = False
        """
        :type map: Map
        """
        self.map = None
        """
        @type dict[string, function]: commands
        """
        self.commands = {}
        for name in dir(self):
            if name.find("command") == 0 and callable(eval("self." + name)):
                command = name[8:]
                self.commands[command] = eval("self." + name)

        """
        @type dict[string, tuple[string, list[string]]: aliases
        """
        self.aliases = {}
        self.process_aliases("default_aliases.txt")

    def process_aliases(self, filename):
        aliasFile = open("config/" + filename, "r")
        for aliasLine in aliasFile:
            (alias, aliasCommand) = map(lambda str: str.strip(), aliasLine.split(":"))
            parameters = filter(len, aliasCommand.split(" "))
            command = parameters.pop(0)
            self.aliases[alias] = (command, parameters)

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

    def play(self):
        self.playing = True
        if self.player.roomId not in self.map.rooms.keys():
            self.player.roomId = 0

        self.playerMoved()
        baseprompt = "Command:"
        while self.playing:
            prompt = "Room: %d %s" % (self.player.roomId, baseprompt)
            command = raw_input(prompt + ">")
            turn_over = self.run_command(command)


    def run_command(self, commandString):
        """
        Attempts to run the entered command.

        To add new commands, add functions to the command dictionary in the init function
        :param string commandString: the enetered command
        :rtype: bool Whether the command consumed the player's turn
        """
        commandWords = commandString.split(" ")
        commandWords = filter(len, map(lambda x: x.strip(), commandWords))
        command = commandWords[0]
        parameters = commandWords[1:]
        if command in self.commands.keys():
            return self.commands[command](*parameters)
        else:
            if command in self.aliases.keys():
                (aliasCommand, aliasParameters) = self.aliases[command]
                parameters = list(aliasParameters) + parameters
                if aliasCommand in self.commands.keys():
                    return self.commands[aliasCommand](*parameters)
            else:
                cprint("Command not found: %s (%s)" % (command, commandString), 'red')

    def command_move(self, direction=None, *args):
        if direction is None:
            print "What direction do you want to move?"
            return False

        if direction in self.map.rooms[self.player.roomId].exits.keys():
            self.player.roomId = self.map.rooms[self.player.roomId].exits[direction]
            self.playerMoved()
            return True
        else:
            print "You can't go that way."
            return False

    def playerMoved(self):
        self.map.rooms[self.player.roomId].print_desc()

    def command_alias(self, alias=None, command=None, *params):
        if alias is None:
            print "Existing aliases:"
            for alias in self.aliases.keys():
                print " %s => %s %s" % (alias, self.aliases[alias][0], " ".join(self.aliases[alias][1]))
            return False

        if command is None:
            print "Syntax: alias <newname> <replacement command>"
            return False

        if alias in self.commands.keys():
            print "You cannot make an alias of an existing command (%s)" % alias
            return False

        if command not in self.commands.keys():
            print "Command not found: %s" % command
            return False

        replaceExisting = False
        if alias in self.aliases.keys():
            replaceExisting = True

        self.aliases[alias] = (command, params)
        print "Alias created: %s for %s %s" % (alias, command, " ".join(params))
        if replaceExisting:
            print "Previous alias updated"
        return False

    def command_quit(self, *args):
        print "You have quit. Thanks for playing!"
        self.playing = False
        return False

    def command_help(self, command=None, *args):
        if command is None:
            print "Command List:"
            for command in self.commands.keys():
                print "  " + command
            print "Type 'help <command>' for more information about each command."
            return False

        if command in self.commands:
            print "Help for '%s':" % (command,)
            if os.path.exists("help/" + command + ".help"):
                with open("help/" + command + ".help") as helpFile:
                    print helpFile.read()
        else:
            print "Unknown command. Type 'help' for a list of all commands."
        return False