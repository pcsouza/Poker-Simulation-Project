import Game, Hand
import numpy as np
import sys

#Class method for betting. Bets at different stages have their own methods to allow
#for expansion into unique methods for each stage of the game.
class BettingMethods(object):
	
	def __init__(self, numplayers):
		self.numplayers = numplayers
		self.NetWinnings = np.zeros((numplayers))
<<<<<<< HEAD
		self.BetProfile = [0 for i in range(numplayers)] #Determines what betting method to use on each player.
=======
		self.BetProfile = [0 for i in range(self.numplayers)] #Default betting behaviour
>>>>>>> Documentation and Linear Tweaks
		self.verbose = False
		if len(self.BetProfile) != self.numplayers: #debugging check
			print "Error: mismatch between betting profile and player size"
			sys.exit()
		else:
			pass
			
	
	def HandBet(self, H):
		for j in range(2):
			for i in list(H.players):
				if self.BetProfile[i] == 1:
					self.LinearBet(i, H, j)
				else: 
					self.SimpleBet(i, H, j)
		if self.verbose == True:
			print "Remaining players:"
			print H.players
			print "Current Bets:"
			print H.StageBet
		else: 
			pass
			
	def FlopBet(self, H):
		for j in range(2):
			for i in list(H.players):
				if self.BetProfile[i] == 1:
					self.LinearBet(i, H, j)
				else: 
					self.SimpleBet(i, H, j)
		if self.verbose == True:
			print "Remaining players:"
			print H.players
			print "Current Bets:"
			print H.StageBet
		else: 
			pass
				
	def TurnBet(self, H):
		for j in range(2):
			for i in list(H.players):
				if self.BetProfile[i] == 1:
					self.LinearBet(i, H, j)
				else: 
					self.SimpleBet(i, H, j)
		if self.verbose == True:
			print "Remaining players:"
			print H.players
			print "Current Bets:"
			print H.StageBet
		else: 
			pass
				
	def RiverBet(self, H):
		for j in range(2):
			for i in list(H.players):
				if self.BetProfile[i] == 1:
					self.LinearBet(i, H, j)
				else: 
					self.SimpleBet(i, H, j)
		if self.verbose == True:
			print "Remaining players:"
			print H.players
			print "Current Bets:"
			print H.StageBet
		else: 
			pass
#Betting method that always bets 10 units and will match any higher bet.
	def SimpleBet(self, player, H, cantraise):
		S = H.Stage
		SB = int(np.amax(H.StageBet[:, S]))
		if cantraise == 0:
			if SB > 10:
				H.StageBet[player, S] = SB
			else:
				H.StageBet[player, S] = 10
		elif cantraise == 1:
			H.StageBet[player, S] = SB
<<<<<<< HEAD
#Betting method that will call if the bet is within a given range of predicted winning chances and fold or raise
#otherwise
=======
			
#Bets with a linear proportion to the chances of winning with a fold/raise threshold
#inversely proportional to the number of players in the game still.	
>>>>>>> Documentation and Linear Tweaks
	def LinearBet(self, player, H, cantraise):
		if H.VictoryChance[player, H.Stage] == 0:
			H.MCAnalysis(100, player)
		else:
			pass
		C = H.VictoryChance[player, H.Stage]
		S = H.Stage
		SB = int(np.amax(H.StageBet[:, S]))
		if cantraise == 0:
			if 100*C < (SB - 100/(len(H.players)*2)):
				H.players.remove(player)
				if self.verbose == True:
					print "Player", player, "folds"
				else:
					pass
			elif 100*C > (SB + 100/(len(H.players)*2)):
				H.StageBet[player, S] = int(100*C)
				if self.verbose == True:
					print "Player", player, "bets", H.StageBet[player, S]
				else:
					pass
			else:
				H.StageBet[player, S] = SB
				if self.verbose == True:
					print "Player", player, "calls for", SB
				else:
					pass
		elif cantraise == 1:
			if 100*C < (SB - 100/(len(H.players)*2)):
				H.players.remove(player)
				if self.verbose == True:
					print "Player", player, "folds"
				else:
					pass
			else:
				H.StageBet[player, S] = SB
				if self.verbose == True:
					print "Player", player, "calls for", SB
				else:
					pass
				
			 
#Monte Carlo analysis of the hand to produce a given player's percieved chances
#of winning (aka. all other player's cards are randomized) 	
	def MCAnalysis(players, Hand, iter, player):
		V = np.zeros((3), int)
		for E in range(iter):
			TestHand = Hand.PlayHand(len(players))
			for i in range(7):
				TestHand.DetAssignCard(player, i,
				(Hand[player, i, 0], Hand[player, i, 1]))
			TestHand.DealAll()
			TestHand.SetVictory()
			V += TestHand.Victory[player]
		C = float((V[1] + V[2]))/V[0]
		if self.verbose == True:
			print "MC analysis for player", player, C
		else:
			pass
		return C
