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

    if guess == doorwithcar:
        return False
    else:
        return True

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

