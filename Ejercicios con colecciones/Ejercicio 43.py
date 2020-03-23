print ("Hola, a continuacion veras una lista con los primeros 20 numeros pares")

lista=[]
suma=0
for i in range(2,41,2):
    lista.append(i)
print(lista)
for j in lista:
    suma+=j

print("Ahora veras la suma de los 20 numeros pares")
print(suma)
