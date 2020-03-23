import random

matriz=[]
suma = 0

for i in range(4):
    matriz.append([0]*4)

for i in range(0,4):
    for j in range(0,4):
        matriz[i][j]=random.randint(1,9)
        if(j > i):
            suma = matriz[i][j]+suma

print ("Veremos una matriz 4X4, la cual esta formada de la siguiente manera " + str(matriz))
print ("A continuacion veremos la suma de la diagonal principal, la cual es " + str(suma))

