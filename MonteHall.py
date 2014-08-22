import random
import math

iterations = (int(1000000))
iterationsfloat = (float(iterations))

should_have_switched = (int(0))
should_have_stayed = (int(0))

def montygame_switch():
	doorwithcar = random.randrange(3) #randomly picks one door to have a car behind
	guess = random.randrange(3) #randomly selects one door for the player
	montyremoves = random.randrange(2) #monty removes one at random, meaning switched answer must be the remaining box
	if guess == 0 and doorwithcar == 0: #ie their guess is box a and answer is behind box a
		if montyremoves == 0:
			switched_answer = 1      #ie switched answer is box b   
		elif montyremoves == 1:
			switched_answer = 2 	#is switched answer is box c
	elif guess == 0 and doorwithcar != 0:
		if doorwithcar == 1:
			switched_answer = 1
		else:
			switched_answer = 2
	elif guess == 1 and doorwithcar == 1: #ie their guess is box b and the answer is behind b
		if montyremoves == 0:
			switched_answer = 0
		elif montyremoves == 1:
			switched_answer = 2
	elif guess ==1 and guess != doorwithcar:
		if doorwithcar == 0:
			switched_answer = 0
		else:
			switched_answer = 2
	elif guess == 2 and guess == doorwithcar: # ie their guess is box c and the answser is behind c
		if montyremoves == 0:
			switched_answer = 0
		elif montyremoves == 1:
			switched_answer = 1
	elif guess == 2 and guess != doorwithcar:
		if doorwithcar == 0:
			switched_answer = 0
		else:
			switched_answer = 1
	# print ("Your guess is %d" % (guess))
	# print ("The door with the car behind it is %d" % (doorwithcar))
	# print ("If you switched your answer would have been %d" % (switched_answer))
	if switched_answer == doorwithcar:
		return True
	else:
		return False

for i in range(iterations):
	if montygame_switch():
		should_have_switched = should_have_switched + 1
	else:
		should_have_stayed = should_have_stayed +1

switched_ratio = ((should_have_switched/iterationsfloat) * 100)
rounded_ratio = str(round(switched_ratio, 2))
print ("You should have stayed %d times" % (should_have_stayed))
print ("You should have switched %d times" % (should_have_switched))
print ("You would have been better switching %s%% of the time" % (rounded_ratio))

