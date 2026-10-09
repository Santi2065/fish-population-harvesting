'''
tomando los datos del lago Andresino
busco la cantidad de peces maxima que se pueden pescar diariamente
para que no se extingan
utilizo CANTIDAD_PECES (cantidad inicial de peces),pesca (la cantidad de pesca diaria),
ALFA (la taza de reproduccion de los peces),BETA (la capacidad de peces que tiene el lago)
y GAMA (proporcion de peces que son comidos por otros depredadores en el lago)
'''
BETA = 24487
# defino la cantidad inicial de peces como el 90% de la capacidad maxima del lago
CANTIDAD_PECES = BETA * 0.9
ALFA = 0.000082
GAMA = 0.1
DIAS = 90
pesca = 0
counter = DIAS
peces_dia = CANTIDAD_PECES
resultado = pesca
# mientras la cantidad de peces sea positiva, voy aumentando de a uno la cantidad pescada por dia,
# reinicio el counter a N dias e igualo el resultado a la cantidad pesca de la iteracion anterior (de esta forma cuando se extingan los peces devuelvo resultado que es la cantidad de pezca que no los extingue)
while peces_dia > 0:
    counter = DIAS
    resultado = pesca
    pesca += 1
    peces_dia = CANTIDAD_PECES
    # Va chequeando que pasen los N dias con el counter, y al mismo tiempo chequea que los peces no se extinguieron para evitar iteraciones extra.
    while counter > 0 and peces_dia > 0:
        counter -= 1
        peces_dia = peces_dia + ALFA * peces_dia * (BETA - peces_dia) - GAMA * peces_dia - pesca
print(f"si se pescan {resultado} peces por dia, no se extinguiran los peces")
    
