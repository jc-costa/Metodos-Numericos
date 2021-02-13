# encondig: utf-8

"""
Seja dy/dx = f(x, y) uma equação diferencial com condições iniciais y(x0)=y0, então as aproximações sucessivas desta equação podem ser dadas por:

y(n+1) = y(n) + h * f(x(n), y(n))

Sendo h = (x(n) – x(0))/n, que indica o tamanho do passo. 
Quanto menor o valor do h escolhido, mais preciso são os resultados e mais tempo de computação é necessário.

Implementaremos o método e iremos usar como exemplo a seguinte questão:

dy/dx =(x + y + xy)
x0 = 0
y0 = 1
h = 0.025
Então, encontre y(0.1).
"""

import math

#aqui a função matemática a ser computada é definida 
def function(x, y):
    return (x + y + x * y) 

def eulerSimples(x0, y0, h, x): 
    yn = y0
    
    #aqui interamos até o ponto que queremos a apróximação
    #y1 = y0 + h * func(x0, y0) 
    #y2 = y1 + h * func(x0, y1)
    #.
    #.
    #.

    while x0 < x: 
        yn1 = yn + h * function(x0, yn) 
        yn = yn1
        x0 = x0 + h #a variável x0 sempre está sendo incrementado o valor de h, então estamos "andando" no eixo x a cada  interação
  
    print("A solução aproximada em x =", x, "é", "%.6f"% yn1) 

valores = input("Forneça valores para x0, y0, h, x: ").split()
x0, y0, h, x = float(valores[0]), float(valores[1]), float(valores[2]), float(valores[3])

eulerSimples(x0, y0, h, x) 
