# utilizo y0 (cantidad inicial de peces),x (la cantidad de pesca diaria),
# alfa (la taza de reproduccion de los peces),beta (la capacidad de peces que tiene el lago)
# y gama(proporcion de peces que son comidos por otros depredadores en el lago)
# para predecir la poblacion de peces
# y armo una tabla con los resultados que muestran la cantidad de peces por el dia

y0 = int(input("Ingrese y0: "))
if y0 < 0:
    print("y0 no puede ser negativo")
    exit()
x= int(input("Ingrese x: "))
if x < 0:
    print("y0 no puede ser negativo")
    exit()
alfa= float(input("Ingrese alfa: "))
beta= int(input("Ingrese beta: "))
gama= float(input("Ingrese gama: "))
n= int(input("Ingrese N: "))
print(" t_i   | y_i   ")
print("-------+-------")
print(f" 0     | {int(y0)}  ")
#pasar a for in range()
for i in range(n):
    i+=1
    y0= y0 + alfa*y0*(beta-y0)-gama*y0-x
    if(y0<0):
        y0=0
    if(i<10):
        print(f" {i}     | {int(y0)}  ")
    else:
        print(f"{i}     | {int(y0)}  ")



