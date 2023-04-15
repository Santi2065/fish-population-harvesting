'''
 utilizo y0 (cantidad inicial de peces),x (la cantidad de pesca diaria),
 alfa (la taza de reproduccion de los peces),beta (la capacidad de peces que tiene el lago)
 y gama(proporcion de peces que son comidos por otros depredadores en el lago)
 para predecir la poblacion de peces
 y armo una tabla con los resultados que muestran la cantidad de peces por el dia
 '''
# pido los datos necesarios por la consola y los valido
while True:
    try:
        cantidad_peces = int(input("Ingrese la cantidad de peces: "))
        if cantidad_peces >= 0:
           break
        else:
           print("la cantidad de peces no puede ser negativa")
    except:
        print("no ingresaste un numero")

while True:
    try:
        pesca = int(input("Ingrese la pesca diaria: "))
        if pesca >= 0:
            break
        else:
            print("la pesca no puede ser negativa")
    except:
        print("no ingresaste un numero")

while True:
    try:
        alfa = float(input("Ingrese la tasa de reproducción de los peces: "))
        if alfa >= 0:
            break
        else:
            print("la tasa de reproduccion no puede ser negativa")
    except:
        print("no ingresaste un numero")

while True:
    try:
        beta = int(input("Ingrese la capacidad del lago: "))
        if beta >= 0:
            break
        else:
            print("la capacidad del lago no puede ser negativa")
    except:
        print("no ingresaste un numero")

while True:
    try:
        gama = float(input("Ingrese la proporción de peces que son comidos por otros depredadores en el lago: "))
        if gama >= 0:
            break
        else:
            print("la proporcion de peces comidos por depredadores no puede ser negativa")
    except:
        print("no ingresaste un numero")

while True:
    try:
        dias = int(input("Ingrese la cantidad de dias: "))
        if dias >= 0:
            break
        else:
            print("la cantidad de dias no puede ser negativa")
    except:
        print("no ingresaste un numero")

# creo una variable peces_dia que voy a ir modificando a medida que pasen los dias e imprimo el principio de la tabla
peces_dia = cantidad_peces
print(" t_i   |   y_i")
print("-------+--------")
# voy imprimiendo la tabla, e haciendo la ecuacion, si el valor de peces_dia es negativo, lo iguala a 0
for i in range(dias+1):
    print(f"{i:2d}     | {int(peces_dia):6d}  ")
    i+=1
    peces_dia = peces_dia + alfa * peces_dia * (beta - peces_dia) - gama * peces_dia - pesca
    if(peces_dia<0):
        peces_dia=0
    