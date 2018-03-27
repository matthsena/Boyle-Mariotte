import math

qnt = input("Digite o número de vezes que deseja executar esse script: ")
qnt = int(qnt)

for i in range(qnt):

	x  = input("Digite o valor x: ")
	sX = input("Digite a incerteza de x: ")
	y  = input("Digite o valor de y: ")
	sY = input("Digite a incerteza de y: ")
	w  = input("Digite o valor de w: ")

	x  = float(x)
	sX = float(sX)
	y  = float(y)
	sY = float(sY)
	w  = float(w)


	total_p = ((sX/x)**2) + ((sY/y)**2)

	total_t = math.sqrt(((w ** 2) * total_p))

	print("\nσPtot·V = ",total_t)

