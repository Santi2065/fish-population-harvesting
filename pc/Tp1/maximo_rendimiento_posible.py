BETA = 24487
Y0 = BETA*0.9
x = 0
ALFA = 0.000082
GAMA = 0.1
N = 90
counter = N
y_i = Y0
resultado=x
while y_i>0:
    counter = N
    resultado = x
    x += 1
    y_i = Y0
    while counter > 0 and y_i > 0:
        counter -= 1
        y_i = y_i + ALFA * y_i * (BETA - y_i) - GAMA * y_i - x
print(f"si se pesca {resultado} peces por dia, no se extinguiran los peces")
    
