# Create a cuadratic.py program that asks the user for three numbers, a, b and c, and calculates the quadratic equation:



print('Introduce los elementos a,b y c para calcular la ecuación de segundo grado')
a= int(input('Valor de "a": '))
b= int(input('Valor de "b": '))
c= int(input('Valor de "c": '))

xa = (-b+(b**2 - (4*a*c))**0.5)/(2*a)
xb = (-b-(b**2 - (4*a*c))**0.5)/(2*a)

print (xa)
print (xb)