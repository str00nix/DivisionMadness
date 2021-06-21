def main():
	maxnum = 1000
	maxnumdiglen = len(str(maxnum))
	
	d = {}
	
	for i in range(2,maxnum+1):
		ar = [a for a in range(2,round(i/2)+1) if not i%a]
		if ar != []:
			d[i] = ar
	
	
	d = {k: v for k, v in sorted(d.items(), key=lambda x: (len(x[1]),x[0]),reverse=True)}
	
	for a in d.items():
		print(f"{a[0]} = {a[1]}")
	
	print()
	
	divisorGroupsByLength = {len(v): [i for i in d.values() if len(v) == len(i)] for k, v in d.items()}
	
	for a in divisorGroupsByLength.items():
		print(f"{a[0]}: {a[1]}\n")

if __name__ == '__main__':
	main()