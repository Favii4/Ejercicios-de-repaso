def fac (*n):
    for x in n:
        factorial=1
    for y in range(1,x+1):
        factorial=factorial*y
    print(factorial)

print("Hola")
resultado=int(input("Por favor ingresa un numero entero "))
fac(resultado)
