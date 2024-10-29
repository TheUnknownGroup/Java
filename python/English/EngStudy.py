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
questions = ['1) Who is a judge presiding over the Salem witch trials along with Deputy Gov. Danforth?',
             '2) As this act opens, what accusations does Giles Corey make?',
             '3) What news do we learn about Rebecca Nurse?',
             '4) When John Proctor arrives at court with Mary Warren, of what does Rev. Parris accuse him?',
             '5) What two pieces of evidence are brought out against Proctor in regard to his Christian Nature?',
             '6) What news does Danforth tell John Proctor about Elizabeth What deal does he try to make about him?',
             '7) What is going to happen to the 91 people who signed the testament stating a good opinion of Elizabeth, Martha Corey, and Rebecca Nurse?',
             '8) Discuss \'Do that which is good, and no harm shall come to thee.\'(page 95)',
             '9) What is Giles Corey\'s proof that Thomas Putnam is \'reaching out for land\'? Why won\'t he reveal his source?',
             '10) What happens to Giles Corey?',
             '11) What is Rev. Hale\'s advice to John Proctor as he is about to read his deposition before the court?',
             '12) What does Danforth think Mary Warren\'s appearance in the court might be?',
             '13) When Mary Warren says that she pretended to faint in court, what is she asked to do? What is the result?',
             '14) What does Abigail do when suspicion that she might be pretending falls on her?',
             '15) What does John Proctor do to discredit her?',
             '16) Who is called to back up John Proctor\'s testimony? What happens?',
             '17) What happens when Rev. Hale states that Abigail has always eemed false to him?',
             '18) What is Mary Warren\'s reaction to Abigail\'s performance?',
             '19) What does John Proctor mean when he says, \'God is dead!\'?',
             '20) What does Hale do when Proctor is arrested?']
# This section is for the answers, there are many so it'll take me a while.
answers = ['a) Giles Corey accuses that Thomas Putnam has been killing his neighbors to get land.', '\n', 'b)', '\n', 'c)', '\n', 'd)',
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # She was condemned to hang because she was accused to witchcraft.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # He has been accused of trying to overthrow the court.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # He doesn\'t go to church and plows on Sundays.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # Elizabeth is pregnant and that she has one year to live for the baby.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # They will arrest and question all 91 people.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # If you are good, then no harm will come. If you do wrong, then bad things will come to you.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # Word of mouth from an honest man. He doesn't want the person to go to jail.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # He gets arrested and charged with comtempt of court.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # He needs a lawyer
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # Mary\'s appearannce might be that Satan is trying to overthrow the court.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # She is asked to faint, but she can\'t.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # Abigail evades or attacks.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # John calls Abigail a *****. He is basically confessing that he commited adultery.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # Elizabeth is called to back up, but she lies and denies it.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # She pretends the bird is attacking.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # She laughs and blames John Proctor.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)', # He means that there is no god in Salem anymore.
           'a)', '\n', 'b)', '\n', 'c)', '\n', 'd)' # Rev. Hale quits the court when John Proctor gets arrested.
           ] 

def start():

start()