"""
Dado o problema o problema de valor inicial qualquer 
dx/dy = f(x, y) e y(0) = 0

O método Runge-Kutta encontra o valor aproximado de y para um determinado x. 
Apenas as equações diferenciais ordinárias de primeira ordem podem ser resolvidas 
usando o método de Runge Kutta de 4ª ordem.

Dado a sua fórmula, a implementação em pytho fica bem direta.
yn+1 = yn + (1/6)*(k1+2K2+2K3+k4)
tn+1 = tn + h

k1 = h*f(tn, y) 
k2 = h*f(tn + (h/2), y + (h/2) * k1) 
k3 = h*f(tn + (h/2), y + (h/2) * k2) 
k4 = h*f(tn + h, y + h*k3)
"""

#esta será a função definida para testarmos o método
def function(x, y): 
    return (x - y + 2) 

def rungeKutta4thOrder(x0, y0, x, h, n): 
    
    y = y0 

    for i in range(1, n + 1): 
        k1 = h * function(x0, y) 
        k2 = h * function(x0 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * function(x0 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * function(x0 + h, y + k3) 
  
        #Atualizando para o próximo valor de y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
  
        #Atualizando para o próximo valor de x 
        x0 = x0 + h 
    return y 

valores = input("Forneça valores para x0, y0, x, h, n: ").split()
x0, y0, x, h, n = float(valores[0]), float(valores[1]), float(valores[2]), float(valores[3]), int(valores[4])

print("O valor de y em x é:", rungeKutta4thOrder(x0, y0, x, h, n))