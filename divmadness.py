def getDivs(lowerlimit = 2, upperlimit = 2, ignorePrimeDivisors = False, ignoreSingleDigitDivisors = False, sortString = None):
	#"ignorePrimeDivisors", "ignoreSingleDigitDivisors" and "sortString" remain unused
	d = {}
	
	for i in range(lowerlimit,upperlimit+1):
		ar = [a for a in range(2,round(i/2)+1) if not i%a]
		if ar != []:
			d[i] = ar
	
	return d

def getDivsByDividentValue(d, fromBiggerToLowerDownwards = True, numberOfDivisorPriority = True):
	#sorted by value of divident first and number of divisors second
	#840 = [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 20, 21, 24, 28, 30, 35, 40, 42, 56, 60, 70, 84, 105, 120, 140, 168, 210, 280, 420]
	return {k: v for k, v in sorted(d.items(), key=lambda x: (len(x[1]),x[0]) if numberOfDivisorPriority else (x[0],len(x[1])), reverse=fromBiggerToLowerDownwards)}

def getDivisorsByDividents():
	#3: [3,6,9]
	#could sort by sum of dividents
	pass

def getDivsByDivisorLength(d, bundleValues = True):
	#2 = [[2,7],[3,5],[2,5],[2,4],[2,3]]
	#or could use tuples to get the value as well
	#2 = [(15,[3,5]), (14,[2,7]), (10,[2,5]), (8,[2,4]), (6,[2,3])]
	if not bundleValues:
		return {len(v): [i for i in d.values() if len(v) == len(i)] for k, v in d.items()} 
	else:
		unsortedBundle = [(k,v) for k, v in d.items()]
		d = {len(a[1]): [i for i in unsortedBundle if len(i[1]) == len(a[1])] for a in unsortedBundle}
		d = dict(sorted(d.items(), key=lambda x: len(x[1]), reverse = True))
		return d

def main():
	#maxnum = 270
	
	#could use this for formatting
	#maxnumdiglen = len(str(maxnum))
	#formatspecifier = str(maxnumdiglen).zfill(2)
	#print(formatspecifier)
	
	minnum = int(input("minnum: "))
	maxnum = int(input("maxnum: "))
	
	choices = ["default","getDivsByDividentValue","getDivsByDivisorLength"]
	
	for i, c in enumerate(choices):
		print(f"{i+1} - {c}")
	
	s = input("Your output choice: ")
	
	while s < '1' or s > str(len(choices)):
		s = input("Input a number in the given range - ")
	
	d = getDivs(minnum,maxnum)
	
	if s == '1':
		pass
	elif s == '2':
		d = getDivsByDividentValue(d)
	elif s == '3':
		d = getDivsByDivisorLength(d)
	else:
		raise Exception('This should not have happened. (Choice number out of range)')
		
	for a in d.items():
		print(f"{a[0]} = {a[1]}")

if __name__ == '__main__':
	main()