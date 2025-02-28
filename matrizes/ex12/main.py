
#exercio 3 nivel basico
def soma_mat(matriz):
    soma = 0
    for l in matriz:
        for c in l:
            soma += c
    return soma

matriz = [    [0,0,0], [0,0,0], [0,0,0] ]
for i in range(3):
	for j in range(3):
		matriz[i][j]=int(input('digite os numeros '))
	print()
print(matriz)

result= soma_mat(matriz)
print(f"A soma de todos os elementos da matriz é: {result}")

#exercico de nivel basico numero 7
# inicializar a matriz 
mat=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
	for j in range(3):
    # atribuindo 1 a matriz principal 
		if i==j:
			mat[i][j] =1
		else:
      # atribuindo 0 aos demais 
			 mat[i][j]=0
      #imprimindo
for i in range(3):
	for c in range(3):
		print(mat[i][c],end=" ")
	print()
	
	#exercico de nivel basico numero 9
#inicializando a matriz 
mat=[[0,0,0],[0,0,0]]
#preenchendo 
for i in range(2):
	for j in range(2):
		 mat[i][j]=int(input('insira o numero '))
#mostrando a matriz completa 
for i in range(2):
  for j in range(2):
    print(mat[i][j],end=" ")
  print()
# imprimindo a matriz principal   
for i in range(2):
	for c in range(2):
	     if i==j:
	     	print(mat[i][c])
