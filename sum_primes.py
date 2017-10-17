import math

'''Sums up prime numbers excluding one'''
#Find checks if a number is prime number
def isprime(num):
	if num < 2:
		return False

	# see if num is divisible by any number up to the square root of num
	for i in range(2, int(math.sqrt(num)) + 1):         
		if num % i == 0:
			return False
	return True
	
#Sum of prime numbers	
def sum(num):
	if num == None:
		return 0
	elif num < 2:
		return num
	else:
		sumd = 0
		for i in range (num):
			if (isprime(i)):
				sumd += i
		return sumd	

if __name__=='__main__':
	print sum(7)