# Instructions
# Let's continue on from the code above.

# Create a guess.py program and type in the following:

# Run the code a few times so that you understand what it does.
# Let's make it so that it's the same guessing game, but there is a new limit to the number of tries (it was infinite before).

# First, introduce a variable called tries at the top and give it a value of 0.
# Then, add the tries variable to the while loop using a relational operator (like you did with guess).

tries = 0
guess = 0

while guess != 6 and tries < 6:
  guess = int(input("Adivina el numero:  "))
  tries += 1
  print("Te quedan",6-tries,"intentos")

if guess == 6:
    print("Lo conseguiste!")
else:
    print("Lo has intendado 6 veces, Intentalo de nuevo")