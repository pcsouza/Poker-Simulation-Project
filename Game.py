import numpy as np
import Hand, Betting

class Game(object):
	
	def __init__(self, numplayers):
		self.numplayers = numplayers
		self.winnings = np.zeros((numplayers))
		self.B = Betting.BettingMethods(numplayers)
		self.BetFuncIndex = [self.B.HandBet, self.B.FlopBet, self.B.TurnBet, 
			self.B.RiverBet]
		self.verbose = False
		
		self.BetProfile = np.zeros((numplayers)) 	#Determines betting behaviour
													#0 is simple bet. Bets 10 and always
													#calls
													#1 is linear bet. Bets based on a 
													#linear relationship to winning chance
													

	
	def PlayHand(self):
		self.B.BetProfile = self.BetProfile
		H = Hand.PlayHand(self.numplayers)
		if self.verbose == True:
			H.verbose = True
			self.B.verbose = True
		else:
			pass

		H.DealHands()
		self.B.HandBet(H)
		
		H.DealFlop()
		self.B.FlopBet(H)

		H.DealTurn()
		self.B.TurnBet(H)
		
		H.DealRiver()
		self.B.RiverBet(H)

		
		H.SetVictory()
		H.CalculateWinnings()
		self.B.NetWinnings += H.Winnings
		if self.verbose == True:
			print "Victory Table"
			print H.Victory
			print "Hand Winnings"
			print H.Winnings
			print "Net Winnings"
			print self.B.NetWinnings
		else:
			pass
	


# 	def DecideBets(stage):  	#stage indicates hand bet, flop bet, etc:
# 		Bets = [0 for i in range(self.numplayers)]
# 		StageBet = 0
# 		for i in H.players:
# 			C = self.BetFuncIndex[stage](i, Hands, Bets, StageBet)
# 			if C == "fold":
# 				
# 			StageBet = max(Bets)
# 		for i in range(self.numplayers):
# 			if Bets[i] == "fold":
# 				H.players.remove(i)
# 		for i in H.players:
# 			Bets[i] = self.BetFuncIndex[stage](i, Hands, Bets, StageBet)
			
			
	