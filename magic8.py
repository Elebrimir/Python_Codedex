# Instructions

# The Magic 8 Ball is a popular office toy and children's toy invented in the 1940's for fortune-telling and advice seeking. 🎱
# It's an oversized 8 ball with some of the following answers:

#     Yes - definitely.
#     It is decidedly so.
#     Without a doubt.
#     Reply hazy, try again.
#     Ask again later.
#     Better not tell you now.
#     My sources say no.
#     Outlook not so good.
#     Very doubtful.

# Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

import random

number = random.randint(1,9)
question = input('Pregunta: ')
answer = ""

if number == 1:
    answer = "Si - definitivamente."
elif number == 2:
    answer = "Es decididamente así"
elif number == 3:
    answer = "Sin duda"
elif number == 4:
    answer = "Respuesta muy poco clara, vuelve a intentarlo"
elif number == 5:
    answer = "Pregúntame de nuevo más tarde"
elif number == 6:
    answer = "Mejor no te lo contaré ahora mismo"
elif number == 7:
    answer = "Mis fuentes dicen que no"
elif number == 8:
    answer = "Las perspectivas son malas"
else:
    answer = "Muy dudoso"

print('Respuesta: ' + answer)