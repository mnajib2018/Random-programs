def krakenCount(m,n):
	Grid = [[0 for col in range(n)] for row in range(m)]
	for col in range(n):
		Grid[0][col] = 1

	for row in range(m):
		Grid[row][0] = 1

	for row in range(m):
		for col in range(n):
			if(row == col):
				Grid[row][col] = 1
				
	for row in range(1,m):
		for col in range(1,n):
			Grid[row][col] = Grid[row-1][col] + Grid[row][col-1] + Grid[row-1][col-1]

	return Grid[m-1][n-1]
