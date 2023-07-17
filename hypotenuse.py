# Create a hypotenuse.py program that asks the user for two numbers, a and b, and calculates the hypotenuse using the Pythagorean equation:

# c=sqrt(a2+b2)


print('Vamos a calcular el valor de la hipotenusa para dos lados dados, a y b')

a = int(input ('Introduce el valor de "a": '))
b = int(input ('Introduce el valor de "b": '))
c = (a**2 + b**2 )**0.5
print(c)