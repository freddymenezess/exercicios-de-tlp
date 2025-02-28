
#exercico de nivel basico numero 7
mat=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
	for j in range(3):
		if i==j:
			mat[i][j] =1
		else:
			 mat[i][j]=0
for i in range(3):
	for c in range(3):
		print(mat[i][c],end=" ")
	print()
