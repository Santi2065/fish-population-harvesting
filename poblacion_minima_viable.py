'''
tomando los datos del lago Andresino
busco la cantidad de peces minima que deberia tener
para que no se extinga con la pesca ilegal
utilizo cantidad_peces (cantidad inicial de peces),x (la cantidad de pesca diaria),
alfa (la taza de reproduccion de los peces),beta (la capacidad de peces que tiene el lago)
y gama (proporcion de peces que son comidos por otros depredadores en el lago)
'''
BETA = 24487
ALFA = 0.000082
GAMA = 0.1
DIAS = 90
cantidad_peces = 0
#defino peces_dia como -1 para que cuando entre al while le sume 1 y considere el caso peces_dia = 0 
peces_dia = -1
x = 237
#defino resultado fuera del while por si no entra, asi no devuelve error
resultado = cantidad_peces
# Entra al while verifica que la cantidad de peces no sea mayor a 0 luego de los 90 dias, de ser asi, suma 1 a la cantidad y0 de peces y se resetea el counter igualandolo nuevamente a DIAS
while peces_dia <= 0:
    counter = DIAS
    cantidad_peces += 1
    resultado = cantidad_peces
    peces_dia = cantidad_peces
    #el proximo while corre la ecuacion de la cantidad de peces N veces gracias al counter, si antes de llegar a DIAS, peces_dia es menor o igual a 0, sale
    while counter > 0 and peces_dia > 0:
        counter -= 1
        peces_dia = peces_dia + ALFA * peces_dia * (BETA - peces_dia) - GAMA * peces_dia - x
print(f"El lago debe tener {resultado} peces como minimo para que no se extingan")