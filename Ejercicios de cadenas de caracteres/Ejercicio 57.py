print ("Hola")

cadena=(input("Escribe una frase o palabra: "))
a=0
for i in cadena:
    if i !=i.lower():
        a+=1
print("La frase tenia " + str(a) + " mayusculas")
