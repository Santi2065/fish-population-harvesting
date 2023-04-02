'''
tomando los datos del lago Andresino
busco la cantidad de peces minima que deberia tener
para que no se extinga con la pesca ilegal
utilizo y0 (cantidad inicial de peces),x (la cantidad de pesca diaria),
alfa (la taza de reproduccion de los peces),beta (la capacidad de peces que tiene el lago)
y gama (proporcion de peces que son comidos por otros depredadores en el lago)
'''
BETA = 24487
ALFA = 0.000082
GAMA = 0.1
N = 90
y0 = 0
#defino y_i como -1 para que cuando entre al while le sume 1 y considere el caso y_i = 0 
y_i = -1
x = 237
#defino resultado fuera del while por si no entra, asi no devuelve error
resultado = y0
# Entra al while verifica que la cantidad de peces no sea mayor a 0 luego de los 90 dias, de ser asi, suma 1 a la cantidad y0 de peces y se resetea el counter igualandolo nuevamente a N
while y_i <= 0:
    counter = N
    y0 += 1
    resultado = y0
    y_i = y0
    #el proximo while corre la ecuacion de la cantidad de peces N veces gracias al counter, si antes de llegar a N, y_i es menor o igual a 0, sale
    while counter > 0 and y_i > 0:
        counter -= 1
        y_i = y_i + ALFA * y_i * (BETA - y_i) - GAMA * y_i - x
print(f"El lago debe tener {resultado} peces como minimo para que no se extingan")