Matrix = [[0 for x in range(0,3)] for x in range(0,3)]
Parse = [[0 for x in range(0,3)] for x in range(0,3)]

Matrix[0][0] = 1
Matrix[0][1] = 2
Matrix[0][2] = 3
Matrix[1][0] = 1
Matrix[1][1] = 1
Matrix[1][2] = 1
Matrix[2][2] = 1
print Matrix

for x in range(0,3):
	for y in range(0,3):
		if Matrix[x][y] == 0:
			Parse[x][y] = 1


for x in range(0,3):
	for y in range(0,3):
		if Parse[x][y] == 1:
			for a in range(0,3):
				Matrix[x][a] = 0
				Matrix[a][y] = 0
				
print Matrix
		
