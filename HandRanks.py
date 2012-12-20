from numpy import array, append, copy, delete, sort, argsort, any, lexsort, arange

def HIGHCARD(Hand):
	G = Hand[argsort(Hand,axis=0)[:,0]]
	return array([0, G[6,0],G[5,0],G[4,0],G[3,0],G[2,0]])

def PAIR(Hand):
	G = Hand[argsort(Hand,axis=0)[:,0]]
	Pair = None
	for i in range(6):
		if G[6-i,0] == G[5-i,0]:
			K = copy(G)
			Kicker = delete(K, [6-i, 5-i], 0)[4,0]
			Pair = array([1,G[6-i][0], Kicker])
			break
	return Pair

def TWOPAIR(Hand):
	G1 = Hand[argsort(Hand,axis=0)[:,0]]
	TwoPair = None
	for i in range(4):
		if G1[6-i,0] == G1[5-i,0]:
			G2 = delete(copy(G1), [6-i, 5-i], 0)
			for j in range(4):
				if G2[4-j,0]==G2[3-j,0]:
					Kicker = delete(copy(G2), [4-j, 3-j], 0)[2,0]
					TwoPair = array([2,G1[6-i][0], G2[4-j][0], Kicker])
					break
		if TwoPair != None:
			break
	return TwoPair
			
def THREEKIND(Hand):
	G = Hand[argsort(Hand,axis=0)[:,0]]
	ThreeKind = None
	for i in range(5):
		if G[6-i,0] == G[5-i,0] and G[6-i,0] == G[4-i,0]:
			Kicker = delete(copy(G), [6-i, 5-i, 4-i], 0)[3,0]
			ThreeKind = array([3, G[6-i,0], Kicker])
			break
	return ThreeKind

def STRAIGHT(Hand):
	G = Hand[argsort(Hand,axis=0)[:,0]]
	Straight = None
	for i in range(3):
		j = 0
		skip = 0
		while j < 5:
			if G[6-i-j-skip,0] == (G[5-i-j-skip,0]+1):
				j += 1
			elif G[6-i-j-skip,0] == G[5-i-j-skip,0]:
				skip += 1		
			else:
				break
		else:
			Straight = array([4,G[6-i,0]])
			break
	return Straight
				
def FLUSH(Hand):
	Flush = None
	G = Hand[lexsort((Hand[:,0], Hand[:,1]))]
	for i in range(3):
		for j in range(4):
			if G[6-i,1] == G[5-i-j,1]:
				pass
			else:
				break
		else:
			Flush = array([5, G[-i-1,0],G[-i-2,0],G[-i-3,0],G[-i-4,0],G[-i-5,0]])
			break

	return Flush

def FULLHOUSE(Hand):
	G = Hand[argsort(Hand,axis=0)[:,0]]
	FullHouse = None
	for i in range(5):
		if G[6-i,0] == G[5-i,0] and G[6-i,0] == G[4-i,0]:
			J = delete(copy(G), [6-i,5-i,4-i], 0)
			for j in range(3):
				if J[3-j,0] == J[2-j,0]:
					FullHouse = array([6, G[6-i,0], J[3-j,0]])
					break
		if any(FullHouse) != None:
			break
	return FullHouse

def FOURKIND(Hand):
	G = Hand[argsort(Hand, axis=0)[:,0]]
	FourKind = None
	for i in range(4):
		if G[6-i,0] == G[5-i,0] and G[6-i,0] == G[4-i,0] and G[6-i,0] == G[3-i,0]:
			Kicker = delete(copy(G), [6-i, 5-i, 4-i, 3-i], 0)[2,0]
			FourKind = array([7, G[6-i,0], Kicker])
			break
	return FourKind

def STRAIGHTFLUSH(Hand):
	H = Hand
	G = H[lexsort((H[:,0], H[:,1]))]
	StraightFlush = None
	for i in range(3):
		for j in range(4):
			if G[6-i,1] == G[5-i-j,1] and G[6-i-j,0] == (G[5-i-j,0] + 1):	
				pass		
			else: 
				break
		else:
			StraightFlush = array([8,G[6-i,0]])
			break

	
	return StraightFlush
