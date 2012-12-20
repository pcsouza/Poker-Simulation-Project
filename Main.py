#This is a basic demonstration of the framework. It produces a 6-player game and plays one hand with
#verbose logging of the hand.

import Game
import numpy as np

print "Main"

#Simple demonstration of the framework
G = Game.Game(6)
G.BetProfile = [1, 1, 1, 1, 1, 1]
G.verbose = True
G.PlayHand()
