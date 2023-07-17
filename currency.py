# Create a currency.py program that asks the user for the amount they have in peso, soles, and reais and calculates the total in USD.

peso = 4044.26
sol = 3.56
reai = 4.80

pesosInput = float(input('Cuantos pesos te han sobrado? '))
solesInput = float(input('Cuantos soles te han sobrado? '))
reaisInput = float(input('Cuantos reais te han sobrado? '))

exchange = (pesosInput/peso)+(solesInput/sol)+(reaisInput/reai)

print(exchange)