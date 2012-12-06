import Game
import numpy as np
import pylab
import matplotlib.mlab as mlab
print "Main"

G = Game.Game(6)
G.BetProfile[0] = 1
G.verbose = True
G.PlayHand()