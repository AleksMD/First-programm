# Inroduction

name = input("Please, write your name!")
print('\tHello, ', name)
while True:
    readyness = input ('Are you ready to start the game?')  
    appropr_ans = 'Yes'
    if readyness.lower() == appropr_ans.lower() :
        print('Lets start!')
        break
    else:
        print('Ok. I am waiting for your next readyness.')
        continue
   

# General variables

rig_an = 0
wr_an = 0


    
   # Questions sector

quest1 = 'What is the name of a language we are studying?'
quest2 = 'How many versions of this language do you know?'
quest3 = 'What is the name of the first computer programm of an average developer?'
quest4 = 'What kind of cycles in Python do you know?'
quest5 = 'What is a transcription of "UTF"?'
quest6 = '"Int" operates with "True" and "False"? Is it correct definintion?'
quest7 = 'What is an origin of the term "bool"?(2 words, branch of math)'
quest8 = 'How long has Python been used?(years, approximately)'
quest9 = 'Which command, "int" or "float", is preferable for work with fractable numbers?'
quest10 = 'Are you sutisfied with my programm?'

# Answers sector

ans1 = 'Python'
ans2 = 'Two'
ans3 = 'Hello, World!'
ans4 = 'While and For'
ans5 = 'Unicode transformation format'
ans6 = 'No'
ans7 = 'Boolean algebra'
ans8 = '30'
ans9 = 'float'
ans10 = 'yes'

#Main sector
while True:
    print(quest1)
    x = input('\tYour answer: ')
    if x.lower() == ans1.lower():
        print('\tGreat!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest2)
    x = input('\tYour answer: ')
    if x.lower() == ans2.lower():
        print('\tExcellent!')
        rig_an +=1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest3)
    x = input('\tYour answer: ')
    if x.lower() == ans3.lower():
        print('\tGood job!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest4)
    x = input('\tYour answer: ')
    if x.lower() == ans4.lower():
        print('\tRight!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest5)
    x = input('\tYour answer: ')
    if x.lower() == ans5.lower():
        print('\tGreat!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest6)
    x = input('\tYour answer: ')
    if x.lower() == ans6.lower():
        print('\tGood result!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest7)
    x = input('\tYour answer: ')
    if x.lower() == ans7.lower():
        print('\tGreat!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest8)
    x = input('\tYour answer: ')
    if x.lower() == ans8.lower():
        print('\tExcellent!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest9)
    x = input('\tYour answer: ')
    if x.lower() == ans9.lower():
        print('\tGood job!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again!')
        wr_an += 1
        break

while True:
    print(quest10)
    x = input('\tYour answer: ')
    if x.lower() == ans10.lower():
        print('\tGreat! It was the last one!')
        rig_an += 1
        break
    else:
        print('\tWrong:(. Try again later! Good luck!')
        wr_an += 1
        break
    
tot_an = rig_an + wr_an
print('\tThank you for participation! Have a good day!')
print('\tRight answers: ', rig_an)
print('\tWrong answers: ', wr_an)
print('\tTotal number of answers: ', tot_an)