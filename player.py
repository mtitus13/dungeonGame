__author__ = 'mtitus'

from actor import Actor

class Player(Actor):
    def __init__(self):
        Actor.__init__(self)
        self.is_player = True