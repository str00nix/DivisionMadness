def main():
	maxnum = 1000
	
	d = {}
	
	for i in range(2,maxnum+1):
		ar = [a for a in range(2,round(i/2)+1) if not i%a]
		if ar != []:
			d[i] = ar
	
	d = {k: v for k, v in sorted(d.items(), key=lambda x: (len(x[1]),x[0]),reverse=True)}
	
	for a in d.items():
		print(f"{a[0]} = {a[1]}")

if __name__ == '__main__':
	main()