# Instructions

# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:
#
#     🦁 Gryffindor
#     🦅 Ravenclaw
#     🦡 Hufflepuff
#     🐍 Slytherin

# Write a sorting_hat.py program that asks the user some questions using int() and places them into one of the Houses based on their answers:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

#     If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
#     Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
#     Else, output the message "Wrong input."

# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

#     If the answer is 1, Hufflepuff +2.
#     Else if answer is 2, Slytherin +2.
#     Else if answer is 3, Ravenclaw +2.
#     Else if answer is 4, Gryffindor +2.
#     Else, output the message "Wrong input."

# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

#     If the answer is 1, Slytherin +4.
#     Else if the answer is 2, Hufflepuff +4.
#     Else if the answer is 3, Ravenclaw +4.
#     Else if the answer is 4, Gryffindor +4.
#     Else, output "Wrong input."

# Lastly, print out the house with the most points!

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
sort_result = 0

print ('Q1) Te gusta la Luz o la Oscuridad?')
print ('1) Luz')
print ('2) Oscuridad')
answer_q1=int(input()) #Dawn/Dusk question answered
print ('Q2) Cuando muera, Quiero que la gente me recuerde como:')
print ('1) El Bueno')
print ('2) El Grande')
print ('3) El Sabio')
print ('4) El Valiente')
answer_q2= int (input ())   #When i'm Dead - Remember Me Question
print ('Q3) Que tipo de instrumento te gusta mas escuchar?')
print ('1) El violin')
print ('2) La trompeta')
print ('3) El piano')
print ('4) El tambor')
answer_q3= int (input ())    #Which Instrument Pleasure your ear Question

if answer_q1 == 1 :
    gryffindor += 1
    ravenclaw += 1
elif answer_q1 == 2 :
    hufflepuff+= 1
    slytherin += 1
else:
    print('Entrada no valida')

if answer_q2 == 1 :
    hufflepuff += 2
elif answer_q2 == 2 :
    slytherin += 2
elif answer_q2 == 3 :
    ravenclaw += 2
elif answer_q2 == 4 :
    gryffindor += 2
else :
    print('Entrada no valida')

if answer_q3 == 1 :
    slytherin += 4
elif answer_q3 == 2 :
    hufflepuff += 4
elif answer_q3 == 3 :
    ravenclaw += 4
elif answer_q3 == 4 :
    gryffindor += 4
else :
    print("Entrada no Valida")

if gryffindor >= hufflepuff and gryffindor >= ravenclaw and gryffindor >= slytherin :
    print ('Irás a la casa 🦁 Griffindor')
elif hufflepuff >= ravenclaw and hufflepuff >= slytherin :
    print ('Irás a la casa 🦡 Hufflepuff')
elif ravenclaw >= slytherin :
    print ('Irás a la casa 🦅 Ravenclaw')
else :
    print ('Irás a la casa 🐍 Slytherin')