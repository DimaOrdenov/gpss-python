import random

def transCREATE(count,timeit):

	ID = count
	TIME = timeit #random.randint(20,50) #random.expovariate(35)
	POS = 'no'
	PRIOR = 0
	NEXTPOS = 1
	
	return ID,TIME,POS,PRIOR,NEXTPOS
	
def printAC(TIME,CURRENT,FUTURE): #After Correction printer
	lengthcur=len(CURRENT)
	lengthfut=len(FUTURE)
	if (len(CURRENT) >= len(FUTURE)):
		length = len(CURRENT)
	else:
		length = len(FUTURE)
	
	for i in range(length):
		print (TIME),
		print ('(Aft. cor.) '),
		if (lengthcur>0 and i<lengthcur):
			print(CURRENT[i]),
			print('	'),
		elif (lengthcur==0 and i<lengthcur):
			print(CURRENT),
			print('				'),
		else:
			print('[]'),
			print('				'),
		if (lengthfut>0 and i<lengthfut): print(FUTURE[i])
		elif (lengthfut==0 and i<lengthfut): print (FUTURE)
		else: print('[]')
		
def printAW(TIME,CURRENT,FUTURE): #After Correction printer
	lengthcur=len(CURRENT)
	lengthfut=len(FUTURE)
	if (len(CURRENT) >= len(FUTURE)):
		length = len(CURRENT)
	else:
		length = len(FUTURE)
		
	"""if (length == 0):
		print (TIME),
		print ('(Aft. watch)'),
		print ('[]'),
		print ('				'),
		print ('[]')"""
		
	for i in range(length):
		print (TIME),
		print ('(Aft. watch)'),
		if (lengthcur>0 and i<lengthcur):
			print(CURRENT[i]),
			print('	'),
		elif (lengthcur==0 and i<lengthcur):
			print(CURRENT),
			print('				'),
		else:
			print('[]'),
			print('				'),
		if (lengthfut>0 and i<lengthfut): print(FUTURE[i])
		elif (lengthfut==0 and i<lengthfut): print (FUTURE)
		else: print('[]')

def CFEtoCCE(TIME,CURRENT,FUTURE):
	if (len(FUTURE)==0):
		return TIME,CURRENT,FUTURE
		
	FUTURE.sort(key=lambda item: item[1])
	TIME = FUTURE[0][1]
	CURRENT.append(FUTURE[0])
	FUTURE.pop(0)
	last = len(CURRENT)
	CURRENT[last-1][1] = 'ASAP'
	
	return TIME,CURRENT,FUTURE


def CCEtoCFE(TIME,NUM,POS,CURRENT,FUTURE):
	if (len(CURRENT)==0):
		return CURRENT,FUTURE
	CURRENT[NUM][1] = TIME
	CURRENT[NUM][2] = POS
	CURRENT[NUM][4] = POS + 1
	FUTURE.append(CURRENT[NUM])
	CURRENT.pop(NUM)
	FUTURE.sort(key=lambda item: item[1])
	
	return CURRENT,FUTURE

			

maxparking = 3
maxshina = 2
maxbalance = 1
maxworker = 2
parking = 0
shina = 0
balance = 0
worker = 0

MEMALL = 0
DONE = 0
QUIT = 0

TIMER = 0
TIME = 0
prevTIME = 0

transCOUNT = 0
transCURRENT = []
transFUTURE = []

print ('TIME		Chain of current events		Chain of future events')
print ('Before EP	'),
print (transCURRENT),
print ('				'),
print (transFUTURE)

while TIMER <= 480:

	rand = TIMER + random.randint(20,50) #random.expovariate(35)
	if (transCOUNT == 0):
		transCOUNT += 1
		ID,TIME,POS,PRIOR,NEXTPOS = transCREATE(transCOUNT,rand)
		transLIST = [ID,TIME,POS,PRIOR,NEXTPOS]
		transFUTURE.append(transLIST)
		print ('After EP	'),
		print(transCURRENT),
		print('				'),
		print(transFUTURE)
		
	TIMER += TIME
	
	#After timer correction
	TIMER,transCURRENT,transFUTURE = CFEtoCCE(TIMER,transCURRENT,transFUTURE)
	if (TIMER <= 480):
		printAC(TIMER,transCURRENT,transFUTURE)
	#print(balance,shina,DONE)
	
	#After overwatch
	i=0
	for trans in transCURRENT:
		i += 1
		if (trans[2] == 'no'):
			MEMALL += 1
			rand = TIMER + random.randint(20,50)
			transCOUNT += 1
			ID,TIME,POS,PRIOR,NEXTPOS = transCREATE(transCOUNT,rand)
			transLIST = [ID,TIME,POS,PRIOR,NEXTPOS]
			transFUTURE.append(transLIST)
			transFUTURE.sort(key=lambda item: item[1])
			if (parking == maxparking):
				QUIT += 1
				transCURRENT.pop(i-1)
				continue
			else:
				parking += 1
				ver1 = random.randint(0,100)
				if (ver1 < 80):
					#MEM80
					if (shina == maxshina):
						trans[2] = 5
						trans[4] = 6
						continue
					else:
						shina += 1
						parking -= 1
						if (worker == maxworker):
							trans[2] = 7
							trans[4] = 8
							continue
						else:
							worker += 1
							#ADVANCE 1
							rand = TIMER + random.randint(25,70)
							transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,8,transCURRENT,transFUTURE)
							continue
				else:
					#MEM20
					ver2 = random.randint(0,100)
					if (ver2 < 50):
						#MEMSH
						if (shina == maxshina):
							trans[2] = 18
							trans[4] = 19
							continue
						else:
							shina += 1
							parking -= 1
							if (worker == maxworker):
								trans[2] = 20
								trans[4] = 21
								continue
							else:
								worker += 1
								#ADVANCE 1
								rand = TIMER + random.randint(25,70)
								transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,21,transCURRENT,transFUTURE)
								continue
					else:
						#MEMB
						if (balance == maxbalance):
							trans[2] = 25
							trans[4] = 26
							continue
						else:
							balance += 1
							parking -= 1
							if (worker == maxworker):
								trans[2] = 27
								trans[4] = 28
								continue
							else:
								worker += 1
								#ADVANCE 2
								rand = TIMER + random.randint(10,20)
								transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,28,transCURRENT,transFUTURE)
								continue
		#print('proverka 5')
		if (trans[2] == 5):
			if (shina == maxshina):
				trans[2] = 5
				trans[4] = 6
				continue
			else:
				shina += 1
				parking -= 1
				if (worker == maxworker):
					trans[2] = 7
					trans[4] = 8
					continue
				else:
					worker += 1
					#ADVANCE 1
					rand = TIMER + random.randint(25,70)
					transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,8,transCURRENT,transFUTURE)
					continue
		#print('proverka 7')					
		if (trans[2] == 7):
			if (worker == maxworker):
				trans[2] = 7
				trans[4] = 8
				continue
			else:
				worker += 1
				#ADVANCE 1
				rand = TIMER + random.randint(25,70)
				transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,8,transCURRENT,transFUTURE)
				continue
		#print('proverka 8')					
		if (trans[2] == 8):
			worker -= 1
			if (balance == maxbalance):
				trans[2] = 10
				trans[4] = 11
				continue
			else:
				balance += 1
				shina -= 1
				if (worker == maxworker):
					trans[2] = 12
					trans[4] = 13
					continue
				else:
					worker += 1
					#ADVANCE 2
					rand = TIMER + random.randint(10,20)
					transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,13,transCURRENT,transFUTURE)
					continue
		#print('proverka 10')					
		if (trans[2] == 10):
			if (balance == maxbalance):
				trans[2] = 10
				trans[4] = 11
				continue
			else:
				balance += 1
				shina -= 1
				if (worker == maxworker):
					trans[2] = 12
					trans[4] = 13
					continue
				else:
					worker += 1
					#ADVANCE 2
					rand = TIMER + random.randint(10,20)
					transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,13,transCURRENT,transFUTURE)
					continue
		#print('proverka 12')					
		if (trans[2] == 12):
			if (worker == maxworker):
				trans[2] = 12
				trans[4] = 13
				continue
			else:
				worker += 1
				#ADVANCE 2
				rand = TIMER + random.randint(10,20)
				transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,13,transCURRENT,transFUTURE)
				continue
		#print('proverka 13')					
		if (trans[2] == 13):
			balance -= 1
			worker -= 1
			DONE += 1
			transCURRENT.pop(i-1)
			continue
		#print('proverka 18')	
		if (trans[2] == 18):
			if (shina == maxshina):
				trans[2] = 18
				trans[4] = 19
				continue
			else:
				shina += 1
				parking -= 1
				if (worker == maxworker):
					trans[2] = 20
					trans[4] = 21
					continue
				else:
					worker += 1
					#ADVANCE 1
					rand = TIMER + random.randint(25,70)
					transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,21,transCURRENT,transFUTURE)
					continue
		#print('proverka 20')			
		if (trans[2] == 20):
			if (worker == maxworker):
				trans[2] = 20
				trans[4] = 21
				continue
			else:
				worker += 1
				#ADVANCE 1
				rand = TIMER + random.randint(25,70)
				transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,21,transCURRENT,transFUTURE)
				continue
		#print('proverka 21')						
		if (trans[2] == 21):
			worker -= 1
			shina -= 1
			DONE += 1
			transCURRENT.pop(i-1)
			continue
			
		if (trans[2] == 25):
			if (balance == maxbalance):
				trans[2] = 25
				trans[4] = 26
				continue
			else:
				balance += 1
				shina -= 1
				if (worker == maxworker):
					trans[2] = 27
					trans[4] = 28
					continue
				else:
					worker += 1
					#ADVANCE 2
					rand = TIMER + random.randint(10,20)
					transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,28,transCURRENT,transFUTURE)
					continue
					
		if (trans[2] == 27):
			if (worker == maxworker):
				trans[2] = 27
				trans[4] = 28
				continue
			else:
				worker += 1
				#ADVANCE 2
				rand = TIMER + random.randint(10,20)
				transCURRENT,transFUTURE = CCEtoCFE(rand,i-1,28,transCURRENT,transFUTURE)
				continue
				
		if (trans[2] == 28):
			worker -= 1
			balance -= 1
			DONE += 1
			transCURRENT.pop(i-1)
			continue
	
	"""rand = TIMER + random.randint(20,50) #random.expovariate(35)
	#lengthfut = len(transFUTURE)
	if (len(transFUTURE) > 0):
		if (rand < transFUTURE[0][1] and rand < 480):
			transCOUNT += 1
			ID,TIME,POS,PRIOR,NEXTPOS = transCREATE(transCOUNT,rand)
			transLIST = [ID,TIME,POS,PRIOR,NEXTPOS]
			transFUTURE.append(transLIST)
			transFUTURE.sort(key=lambda item: item[1])
	elif (rand < 480):
		transCOUNT += 1
		ID,TIME,POS,PRIOR,NEXTPOS = transCREATE(transCOUNT,rand)
		transLIST = [ID,TIME,POS,PRIOR,NEXTPOS]
		transFUTURE.append(transLIST)
		transFUTURE.sort(key=lambda item: item[1])"""
	
	if (TIMER <= 480):
		printAW(TIMER,transCURRENT,transFUTURE)
	#print(balance,shina,DONE)
	print('')

print('All clients '),
print(MEMALL)
print('Clients remained w/ service '),
print(DONE)
print('Clients remained w/o service '),
print(QUIT)

	
	
	
	