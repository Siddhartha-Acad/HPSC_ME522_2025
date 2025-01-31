x0 = 1.0	# initial guess of the root.
s = 2.0		# number of which square root to be calculated.

for i in range(20):				# starting the loop.
	x0 = 0.5 * (x0 + s/x0)		# updating the value of root.
	print(f'{i=}: {x0=}')		# printing info.

