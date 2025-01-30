x0 = 1.0
s = 2.0

for i in range(20):
	x0 = 0.5 * (x0 + s/x0)
	print(f'{i=}: {x0=}')

