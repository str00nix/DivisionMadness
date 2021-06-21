def getDivs(upperlimit = 2, ignorePrimeDivisors = False, removeSingleDigitDivisors = False):
	pass

def getDivsByDividentValue():
	#sorted by value of divident first and number of divisors second
	#840 = [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 20, 21, 24, 28, 30, 35, 40, 42, 56, 60, 70, 84, 105, 120, 140, 168, 210, 280, 420]
	pass

def getDivisorsByDividents():
	#3: [3,6,9]
	#if it is sorted by length then "2" would be at the top every time
	#could sort by sum of dividents
	pass

def getDivsByDivisorLength():
	#2 = [[2,7],[3,5],[2,5],[2,4],[2,3]]
	#or could use tuples to get the value as well
	#2 = [(15,[3,5]), (14,[2,7]), (10,[2,5]), (8,[2,4]), (6,[2,3])]
	pass

def main():
	maxnum = 27
	
	#could use this for formatting
	#maxnumdiglen = len(str(maxnum))
	#formatspecifier = str(maxnumdiglen).zfill(2)
	#print(formatspecifier)
	
	d = {}
	
	for i in range(2,maxnum+1):
		ar = [a for a in range(2,round(i/2)+1) if not i%a]
		if ar != []:
			d[i] = ar
	
	d = {k: v for k, v in sorted(d.items(), key=lambda x: (len(x[1]),x[0]),reverse=True)}
	
	for a in d.items():
		print(f"{a[0]} = {a[1]}")
		
	print()
		
	#instead of just a list, get the divident as well
	divisorGroupsByLength = {len(v): [i for i in d.values() if len(v) == len(i)] for k, v in d.items()}
	
	for a in divisorGroupsByLength.items():
		print(f"{a[0]} = {a[1]}")

if __name__ == '__main__':
	main()