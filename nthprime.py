## Calculates nth prime number

import math

def prime_test(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0 and num != i:
            return False
    return True

def primeLength(n): # finds how many prime numbers below n
	squareofuser = math.sqrt(n)
	roundsquare = int(round(squareofuser))
	primes = [False] + [False] + [True] * (n-1)
	for i in range(roundsquare+1):
		if primes[i]:
			for i in range(i*i,n+1,i):
				primes[i] = False
	numberedPrimes = [i for i,x in enumerate(primes) if x == True]
	length = len(numberedPrimes)
	lastprime = numberedPrimes[-1]
	print ("There are " + str(length) + " primes under your number")
	print ("And the highest one is " + str(numberedPrimes[-1]))
	# print (numberedPrimes)
	# print (primes)
	print (sum(numberedPrimes))


def primeNumber(n): # prints highest prime to number n
	squareofuser = math.sqrt(n)
	roundsquare = int(round(squareofuser))
	primes = [False] + [False] + [True] * (n-1)
	for i in range(roundsquare):
		if primes[i]:
			for i in range(i*i,n+1,i):
				primes[i] = False
	numberedPrimes = [i for i,x in enumerate(primes) if x == True]
	print (numberedPrimes[-1])

def primeTo(n): # finds up to which number we need to test to find nth prime
	x = 1
	while primeLength(x) < n:
		x = x+1
	print (x)

primeLength(2000000)

