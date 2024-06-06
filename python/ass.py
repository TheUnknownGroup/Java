
def get_choice():
    choice = input("Do you want ass? (yes/no): ")
    if choice in ("yes", "Yes", "y", "sure"):
        print("Sorry, there is no ass in stock.")
    else:
        print("Well, you're in luck! We have cake instead.")
get_choice()

questions = input("Do you have any other questions? (yes/no): ")
if questions in ("yes", "Yes", "y", "sure"):
    get_choice()
else:
    print('Byeee!')