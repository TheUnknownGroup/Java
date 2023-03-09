
# Online IDE - Code Editor, Compiler, Interpreter

question1 = 'What is the element name for Fe?'
question2 = 'What are positive atoms?'
question3 = 'What are negative atoms?'

answers1 = 'Iron'
answers2 = 'Protons','protons'
answers3 = 'Electrons','electron'

print(question1)
print('a) Iron')
print('b) Copper')
print('c) Oxygen')
print('d) Phosphorus')
answer = input()
if answer == answers1:
    print ('Congrats, You got this correct!')