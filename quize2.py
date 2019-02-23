#quize2.0 
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

    # Counting variables

righ_an = 0
wr_an = 0

#Answers Database
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

#Questions database

quize_dict = {"Question 1: 'What is the name of a language we are studying?'" : ans1,
"Question 2: 'How many main versions of this language do you know?'" : ans2, 
"Question 3: 'What is the name of the first computer programm of an average developer?'" : ans3, 
"Question 4: 'What kind of cycles in Python do you know?(... and ...)'" : ans4, 
"Question 5: 'What is a transcription of 'UTF'?'" : ans5, 
"Question 6: 'Int' operates with 'True' and 'False'? Is it correct definintion?(Yes or No)'" : ans6, 
"Question 7: 'What is an origin of the term 'bool'?(2 words, branch of math)'" : ans7,
"Question 8: 'How long has Python been used?(years, approximately)'" : ans8, 
"Question 9: 'Which command, 'int' or 'float', is preferable for work with fractable numbers?'" : ans9,
"Question 10: 'Are you sutisfied with my programm?'" : ans10,  
}

for key, value in quize_dict.items():
    print(key)
    user_answer = input('Your answer: ')
    if value.lower() == user_answer:
        print('You are right!')
        righ_an += 1
        
    else:
        print('Try again later!')
        wr_an += 1

tot_an = righ_an + wr_an
print('\tThank you for participation! Have a good day!')
print('\tRight answers: ', righ_an)
print('\tWrong answers: ', wr_an)
print('\tTotal number of answers: ', tot_an)