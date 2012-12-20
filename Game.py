#Game method object. Each game has its own betting method, so multiple game objects with unique betting behaviours
#can be be initialized.

import numpy as np
import Hand, Betting

#Game object. This contains the main method to run a hand which is called repeatedly
#to play the game.
#Contains its own betting method so multiple game objects can be initialized with unique
#betting patterns
class Game(object):
	
	def __init__(self, numplayers):
		self.numplayers = numplayers				#Number of players in the game
		self.winnings = np.zeros((numplayers))			#Array storing the running total of all winnings
		self.B = Betting.BettingMethods(numplayers)		#Initializes the betting method. Thus adaptive
									#methods persist throughout the game.
		self.BetFuncIndex = [self.B.HandBet, self.B.FlopBet, self.B.TurnBet, 
			self.B.RiverBet]				
		self.verbose = False					#Trigger for verbose logging
		
		self.BetProfile = np.zeros((numplayers)) 	#Determines betting behaviour
													#0 is simple bet. Bets 10 and always
													#calls
													#1 is linear bet. Bets based on a 
													#linear relationship to winning chance
													

#Main game method. Game is played by repeated calling of the PlayHand function.	
	def PlayHand(self):
		self.B.BetProfile = self.BetProfile
		H = Hand.PlayHand(self.numplayers)	#Initialize a Hand object with all its methods
		if self.verbose == True:		#Trigger verbose logging in other methods
			H.verbose = True
			self.B.verbose = True
		else:
			pass
		
		#Deal cards and betting actions.
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
	



			
			
	
