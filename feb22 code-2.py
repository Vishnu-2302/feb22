n=int(input('enter the value : '))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=' ')
	print()
for l in range(1,n+1):
	for m in range(1,n-l+1):
		print(m,end=' ')
	print()

