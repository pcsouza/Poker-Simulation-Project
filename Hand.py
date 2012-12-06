from __future__ import division
import numpy as np
import HandRanks as HR
import random as rn
import Betting as B


class PlayHand(object):
	
	def __init__(self, numplayers):
		self.players = range(numplayers)
		self.numplayers = numplayers
		self.HandEval = [HR.STRAIGHTFLUSH, 
			HR.FOURKIND, 
			HR.FULLHOUSE, 
			HR.FLUSH, 
			HR.STRAIGHT, 
			HR.THREEKIND, 
			HR.TWOPAIR, 
			HR.PAIR, 
			HR.HIGHCARD]
		self.CardPop = [(i, j) for i in range(1,14) for j in range(1,5)]
		self.Hands = np.zeros((numplayers, 7, 2), int)
		rn.seed()
		self.Victory = np.zeros((numplayers,2),int)
		self.CurrentBets = np.zeros((numplayers))
		self.Winnings = np.zeros((numplayers))
		self.VictoryChance = np.zeros((numplayers, 4))
		self.Stage = 0
		self.StageBet = np.zeros((numplayers, 4))
		self.verbose = False
		
	def RnAssignCard(self, player, cardpos):
		if cardpos < 2:
			if self.Hands[player, cardpos, 0] == 0:
				C = rn.choice(self.CardPop)
				self.Hands[player, cardpos] = C
				self.CardPop.remove(C)
			else:
				pass
		if cardpos > 1:
			for i in self.players:
				if self.Hands[player, cardpos, 0] == 0:
					pass
				else:
					break
			else:
				C = rn.choice(self.CardPop)
				self.Hands[:, cardpos] = C
				self.CardPop.remove(C)
				
	def DetAssignCard(self, player, cardpos, C):
		if C[0] == 0:
			pass
		elif self.Hands[player, cardpos, 0] == 0:
			if cardpos < 2:
				self.Hands[player, cardpos] = C
			else:
				self.Hands[:, cardpos] = C
			self.CardPop.remove(C)
		else:
			pass
				
	def DealHands(self):
		for i in self.players:
			for j in range(2):
				self.RnAssignCard(i, j)
		if self.verbose == True:
			print "Current hands and table:"
			print self.Hands
		else:
			pass
				
	def DealFlop(self):
		for i in range(2,5):
			self.RnAssignCard(0, i)
		self.Stage += 1
		if self.verbose == True:
			print "Current hands and table:"
			print self.Hands
		else:
			pass
	
	def DealTurn(self):
		self.RnAssignCard(0, 5)
		self.Stage += 1
		if self.verbose == True:
			print "Current hands and table:"
			print self.Hands
		else:
			pass
		
	def DealRiver(self):
		self.RnAssignCard(0, 6)
		self.Stage += 1
		if self.verbose == True:
			print "Current hands and table:"
			print self.Hands
		else:
			pass
	
	def DealAll(self):
		for i in self.players:
			for j in range(2):
				self.RnAssignCard(i, j)
		for i in range(1, 7):
			self.RnAssignCard(self.players[0], i)
		self.Stage = 3
	
	def SetVictory(self):
		self.Victory[:,0] = 1
		Ranks = np.zeros((self.numplayers, 6), dtype = np.ndarray)
		for i in self.players:
			R = None
			for j in self.HandEval:
				R = j(self.Hands[i])
				if R == None:
					pass
				else:
					break
			for j in range(np.shape(R)[0]):
				Ranks[i, j] = R[j]
		
		PEval = list(self.players)
		for Trait in range(6):	
			Tmax = np.amax(Ranks[PEval,Trait])
			for i in list(PEval):
				if Ranks[i,Trait] < Tmax:
					PEval.remove(i)
				else:
					pass

		self.Victory[PEval, 1] = 1
			
	def CalculateWinnings(self):
		for i in range(self.numplayers):
			self.CurrentBets[i] = np.sum(self.StageBet[i])
		self.Winnings -= self.CurrentBets
		self.Winnings += self.Victory[:,1]*np.sum(self.CurrentBets)/np.sum(self.Victory[:,1])
		
		
			
	def MCAnalysis(self, iter, player):
		V = np.zeros((2), int)
		for E in range(iter):
			TestHand = PlayHand(len(self.players))
			for i in range(7):
				TestHand.DetAssignCard(0, i,
				(self.Hands[player, i, 0], self.Hands[player, i, 1]))
			TestHand.DealAll()
			TestHand.SetVictory()
			V += TestHand.Victory[0]
		C = V[1]/V[0]
		self.VictoryChance[player, self.Stage] = C
		if self.verbose == True:
			print "Player:", player, "Predicted chance:", C

		else:
			pass			
	

			
			

				
					
				
			
				
			
			

		
		