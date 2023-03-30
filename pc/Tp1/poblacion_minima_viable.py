# tomando los datos del lago Andresino
# busco la cantidad de peces minima que deberia tener de peces
# para que no se extinga con la pesca ilegal
# utilizo y0 (cantidad inicial de peces),x (la cantidad de pesca diaria),
# alfa (la taza de reproduccion de los peces),beta (la capacidad de peces que tiene el lago)
# y gama(proporcion de peces que son comidos por otros depredadores en el lago)

y0 = 0
BETA = 24487
x= 237
ALFA = 0.000082
GAMA = 0.1
N= 90
y_i=-1
resultado=y0
while y_i<0:
    counter=N
    y0+=1
    resultado=y0
    y_i=y0
    while counter>0 and y_i>0:
        counter-=1
        y_i = y_i + ALFA * y_i * (BETA - y_i) - GAMA * y_i - x
print(resultado)