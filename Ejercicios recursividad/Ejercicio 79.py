def suma(num):
    if(num == 1):
        return 1
    else:
        return num + suma(num-1)

num = int(input("Ingrese un numero "))
print("La suma de los numeros de 1 hasta "+str(num)+" es de "+str(suma(num)))
