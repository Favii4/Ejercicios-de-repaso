import math

dis = 0

def dis(x1,x2,y1,y2):

    dis = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))

    return dis

print("Hola")
a = input("Ingresa la coordenada x1: ")
b = input("Ingresa la coordenada y1: ")
c = input("Ingresa la coordenada x2: ")
d = input("Ingresa la coordenada y2: ")

x1 = float(a)
y1 = float(b)
x2 = float(c)
y2 = float(d)

print("La distancia que hay entre los puntos es de: " +str(dis(x1,x2,y1,y2)))
