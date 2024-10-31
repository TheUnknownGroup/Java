import time
# import openpyxl

global points
points = 0

# This is used so then we can seperate the questions, answers & beginning prompts.
line = '------'

# This is going to be used for the beginning prompt inputs.
yeses = ['yes', 'y', 'Yes', 'Y', 'yeah', 'Yeah', 'yup', 'Yup', 'yep', 'Yep', 'sure', 'Sure']
nos = ['no', 'n', 'No', 'N', 'nope', 'Nope']

# Beginning prompts for the user.
ques1 = "Are you here to study for the English quiz?"
inpY = "Alright! Lets get to it then!"
inpN = "Aww alright, take care!"
welcome = "Welcome to the study part!"

# Questions area, currently there will not be more than 1 questions variable as I did not seem that it was important.
questions = ['1) As this act opens, what accusations does Giles Corey make?',
             '2) What news do we learn about Rebecca Nurse?',
             '3) When John Proctor arrives at court with Mary Warren, of what does Rev. Parris accuse him?',
             '4) What two pieces of evidence are brought out against Proctor in regard to his Christian Nature?',
             '5) What news does Danforth tell John Proctor about Elizabeth What deal does he try to make about him?',
             '6) What is going to happen to the 91 people who signed the testament stating a good opinion of Elizabeth, Martha Corey, and Rebecca Nurse?',
             '7) Discuss \'Do that which is good, and no harm shall come to thee.\'(page 95)',
             '8) What is Giles Corey\'s proof that Thomas Putnam is \'reaching out for land\'? Why won\'t he reveal his source?',
             '9) What happens to Giles Corey?',
             '10) What is Rev. Hale\'s advice to John Proctor as he is about to read his deposition before the court?',
             '11) What does Danforth think Mary Warren\'s appearance in the court might be?',
             '12) When Mary Warren says that she pretended to faint in court, what is she asked to do? What is the result?',
             '13) What does Abigail do when suspicion that she might be pretending falls on her?',
             '14) What does John Proctor do to discredit her?',
             '15) Who is called to back up John Proctor\'s testimony? What happens?',
             '16) What happens when Rev. Hale states that Abigail has always eemed false to him?',
             '17) What is Mary Warren\'s reaction to Abigail\'s performance?',
             '18) What does John Proctor mean when he says, \'God is dead!\'?',
             '19) What does Hale do when Proctor is arrested?']
# This section is for the answers, there are many so it'll take me a while. # Its taken me over 7 hours...
answers = ['a) Giles Corey accuses that Thomas Putnam has been killing his neighbors to get land.', '\n', 'b) He needs a lawyer.', '\n', 'c) Word of mouth from an honest man. He doesn\'t want the person to go to jail.', '\n', 'd) She was condemned to hang because she was accused to witchcraft.',
           'a) Elizabeth is called to back up Proctor\'s statements, but she lies and denies it.', '\n', 'b) She pretends the bird is attacking.', '\n', 'c) She was condemned to hang because she was accused to witchcraft.', '\n', 'd) He doesn\' go to church and plows on Sundays.',
           'a) He gets arrested and charged with contempt of court.', '\n', 'b) He has been accused of trying to overthrow the court.', '\n', 'c) Elizabeth is pregnant and that she has one year to live for the baby.', '\n', 'd) Elizabeth is called to back up Proctor\'s statements, but she lies and denies it.',
           'a) Mary\'s appearance might be that Satan is trying to overthrow the court.', '\n', 'b) Rev. Hale quits the court when John Proctor gets arrested.', '\n', 'c) Word of mouth from an honest man. He doesn\'t want the person to go to jail.', '\n', 'd) He doesn\'t go to church and plows on Sundays.',
           'a) John calls Abigail a *****. He is basically confessing that he commited adultery.', '\n', 'b) He gets arrested and charged with contempt of court', '\n', 'c) Elizabeth is pregnant and that she has one year to live for the baby.', '\n', 'd) Giles Corey accuses that Thomas Putnam has been killing his neighbors to get land.',
           'a) They will arrest and question all 91 people.', '\n', 'b) He means that there is no God in Salem anymore.', '\n', 'c) If you are good, then no harm will come. If you do wrong, then bad things will come to you.', '\n', 'd) He has been accused of trying to overthrow the court.',
           'a) If you are good, then no harm will come. If you do wrong, then bad things will come to you.', '\n', 'b) She pretends the bird is attacking.', '\n', 'c) She is asked to faint, but she can\'t.', '\n', 'd) Rev. Hale quits the court when John Proctor gets arrested.',
           'a) Elizabeth is called to back up Proctor\'s statements, but she lies and denies it.', '\n', 'b) Word of mouth from an honest man. He doesn\'t want the person to go to jail.', '\n', 'c) He needs a lawyer.', '\n', 'd) She is asked to faint, but she can\'t',
           'a) Giles Corey accuses that Thomas Putnam has been killing his neighbors to get land.', '\n', 'b) He has been accused of trying to overthrow the court.', '\n', 'c) He gets arrested and charged with comtempt of court.', '\n', 'd) Mary\'s appearance might be that Satan is trying to overthrow the court.', 
           'a) She is asked to faint, but she can\'t', '\n', 'b) He needs a lawyer', '\n', 'c) Abigails evades or attacks.', '\n', 'd) They will arrest and question all 91 people.',
           'a) She laughs and blames John Proctor.', '\n', 'b) Mary\'s appearannce might be that Satan is trying to overthrow the court.', '\n', 'c) She pretends the bird is attacking.', '\n', 'd) If you good, then no harm will come. If you do wrong, then bad things will come to you.',
           'a) Elizabeth is called to back up Proctor\'s statements.', '\n', 'b) He has been accues of trying to overthrow the court.', '\n', 'c) Giles Corey accuses that Thomas Putnam has been killing his neighbors to get land.', '\n', 'd) She is asked to faint, but she can\'t.', 
           'a) They will arrest and question all 91 people.', '\n', 'b) Abigail evades or attacks.', '\n', 'c) She was condemned to hang because she was accused to witchcraft.', '\n', 'd) Rev. Hale quits the court when John Proctor gets arrested.',
           'a) She laughs and blames John Proctor.', '\n', 'b) He needs a lawyer.', '\n', 'c) John calls Abigail a *****. He is basically confessing that he committed adultery.', '\n', 'd) Word of mouth from an honest man. He doesn\' want the person to go to jail.',
           'a) She pretends the bird is attacking.', '\n', 'b) He doesn\' go to church and plows on Sundays.', '\n', 'c) John calls Abigail a *****. He is basically confessing that he committed adultery.', '\n', 'd) Elizabeth is called to back up Proctor\'s statements, but she lies and denies it.',
           'a) Elizabeth is pregnant and that she has one year to live for the baby.', '\n', 'b) He means that there is no God in Salem anymore.', '\n', 'c) She pretends the bird is attacking.', '\n', 'd) He needs a lawyer.', 
           'a) She laughs and blames John Proctor.', '\n', 'b) He needs a lawyer', '\n', 'c) He doesn\'t go to church and plows on Sundays.', '\n', 'd) Elizabeth is pregnant and that she has one year to live for the baby.',
           'a) Rev. Hale quits the court when John Proctor gets arrested.', '\n', 'b) He means that there is no God in Salem anymore.', '\n', 'c) She was condemned to hang because was accused to witchcraft.', '\n', 'd) He needs a lawyer.',
           'a) He gets arrested and charged with contempt of court.', '\n', 'b) He doesn\'t go to church and plows on Sundays.', '\n', 'c) He means that there is no God in Salem anymore.', '\n', 'd) Rev. Hale quits the court when John Proctor gets arrested.'] 

def ask_questions():
    print(welcome); time.sleep(1)
    print(questions[0])
    for s in answers[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['a','A']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1

def start():
    print(ques1); time.sleep(1)
    ans1A = input(''); time.sleep(1)
    if ans1A in yeses:
        print(inpY); print(line); time.sleep(1); ask_questions()
    elif ans1A in nos:
        print(inpN); time.sleep(1); exit()
    else:
        print('Please put words like: yes, Yes, y, sure. Or: no, No, n, nope.'); time.sleep(1); start()
start()