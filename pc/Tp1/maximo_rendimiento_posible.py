'''
tomando los datos del lago Andresino
busco la cantidad de peces maxima que se pueden pescar diariamente
para que no se extingan
utilizo y0 (cantidad inicial de peces),x (la cantidad de pesca diaria),
alfa (la taza de reproduccion de los peces),beta (la capacidad de peces que tiene el lago)
y gama (proporcion de peces que son comidos por otros depredadores en el lago)
'''

BETA = 24487
# defino la cantidad inicial de peces como el 90% de la capacidad maxima del lago
Y0 = BETA * 0.9
ALFA = 0.000082
GAMA = 0.1
N = 90
x = 0
counter = N
y_i = Y0
resultado = x
# mientras la cantidad de peces sea positiva, voy aumentando de a uno la cantidad pezcada por dia,
# reinicio el counter a N dias e igualo el resultado a la cantidad x de la iteracion anterior (de esta forma cuando se extingan los peces devuelvo resultado que es la cantidad de pezca que no los extingue)
while y_i > 0:
    counter = N
    resultado = x
    x += 1
    y_i = Y0
    # Va chequeando que pasen los N dias con el counter, y al mismo tiempo chequea que los peces no se extinguieron para evitar iteraciones extra.
    while counter > 0 and y_i > 0:
        counter -= 1
        y_i = y_i + ALFA * y_i * (BETA - y_i) - GAMA * y_i - x
print(f"si se pescan {resultado} peces por dia, no se extinguiran los peces")
    
