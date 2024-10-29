import time
import openpyxl

# This is used so then we can seperate the questions, answers & beginning prompts.
line = '------'
# Beginning prompts for the user.
ques1 = "Are you here to study for the English quiz?"
inpY = "Alright! Lets get to it then!"
inpN = "Aww alright, take care!"
welcome = "Welcome to the study part!"
# Questions area, currently there will not be more than 1 questions variable as I did not seem that it was important.
questions = ['Who is a judge presiding over the Salem witch trials along with Deputy Gov. Danforth?',
             'Who is the head judge of the Salem witch trials, and thinks they are fair-minded?',
             'As this act opens, what accusations does Giles Corey make?',
             'What news do we learn about Rebecca Nurse?',
             'When John Proctor arrives at court with Mary Warren, of what does Rev. Parris accuse him?',
             'What two pieces of evidence are brought out against Proctor in regard to his Christian Nature?',
             'What news does Danforth tell John Proctor about Elizabeth What deal does he try to make about him?',
             'What is going to happen to the 91 people who signed the testament stating a good opinion of Elizabeth, Martha Corey, and Rebecca Nurse?',
             'Discuss \'Do that which is good, and no harm shall come to thee.\'(page 95)',
             'What is Giles Corey\'s proof that Thomas Putnam is \'reaching out for land\'? Why won\'t he reveal his source?']