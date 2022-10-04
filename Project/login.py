from quiz import Question
from numberGuess import Guessing

#quiz_game = Question
check = False
check_login = False
quizGame = Question
numberGuessGame = Guessing
global user_name
isfound = False

global isagain, selectGame, LOL
isagain = True
selectGame = 0
# LOL = True

def register():
    with open('Data_User.txt', 'r', encoding='utf8') as f:
        data = f.read()
        data = data.split("\n")
        user_name = input("✡ Create Username ✡ : ")
        f = open('Data_User.txt', 'a',encoding='utf8')
        f.write("\n" + user_name)
        f.close()
        print('≽  Registered. Please Log-in  ≼')
        #print()
        #login()
    return user_name


def login():
    user_name = input("✥ Enter Username ✥ : ")
    global check
    with open('Data_User.txt', 'r', encoding='utf8') as f:
        data = f.read()
        data = data.split("\n")
        if user_name in data:
            print()
            print(f"❖  Hello {user_name} We glad that you're here!  ❖")
            check = True
            #print(user_name)
            return user_name
        else:
            print("Sorry. We could not find a user (。-`ω '-)")
            print("Please try agiain")
            print()
            choices()
            #check = False
            #return check
        f.close()


def choices():
    global check_login
    check_choice = False
    print("\t\tWelcome!")
    print("Please choose Log-in or Register.")
    print("* * * * * * * * * * * * * * * * * * * * * * *")
    while check_choice == False:
        choices = input(" >>> For Register Type 1 and For Log-in Type 2 For Exit Type 0 : ")
        if choices == "0":
            print("EXIT ....")
            check_choice = True
            exit()
        elif choices == "1":
            user_name = register()
            check_choice = True
            return user_name
        elif choices == "2":
            while check == False:
                if check == False:
                    user_name = login()
                    check_login = True
                    check_choice =True
                    return user_name
                elif check == True:
                    break
        else:
            print("Did you forget something ?")
            print("LOADING ....")
            

def menu():
    print()
    print("-" * 30)
    print("✩ Quiz Game press '1' ✩")
    print("✩ Guess Number Game press '2' ✩")
    print("✩ Leader board press '3' ✩")
    print("✩ Exit press '0' ✩")


def playAgain():
    LOL = True
    isagain = True
    while LOL:
        print()
        choose = input("If you want to play again press  ▶ Yes ◀ , if not press  ▶ No ◀ : ")
        choose = choose.lower()
        if choose == "yes":
            isagain = True
            LOL = False
            return isagain
        elif choose == "no":
            print("EXIT ....")
            LOL = False
            isagain = False
            return isagain
        else:
            print("Enter 'Yes' or 'No' ")
            continue


def scoreQuiz():
    with open('data_quiz.txt','r', encoding='utf8') as sc:
        print(sc.read())


def scoreGuess():
    with open('data_numguess.txt', 'r', encoding='utf8') as sc:
        print(sc.read())


def scoreGames():
    check_score = False
    while check_score == False:
        print("✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴")
        print("Press '1' for Quiz Game press '2' for Guess Number Game.")
        chooseGame = input(" ✦ What game do you want to check score ✦ : ")
        if chooseGame == "1":
            print()
            print("----- Score Quiz Game -----")
            scoreQuiz()
            check_score = True
        elif chooseGame == "2":
            print()
            print("----- Score Guess Number Game -----")
            check_score = True
            scoreGuess()
        else:
            #print("please enter number 1 or 2")
            print("Did you forget something ?")
            print("LOADING ....")
            print()


#----------- MAIN -----------#

user = choices()
#print(user)
if check_login == False:
    login()

#print(user)
while isagain == True:
    menu()
    choose = input(">> Choose what you want : ")
    if choose == "1":
        print()
        print("------ Welcome to Quiz Game! ------")
        print(": ̗̀➛ Answer tricky questions and test your knowlegde! ")
        print()
        quizGame.quiz_game(user)
        isagain = playAgain()

    elif choose == "2":
        print()
        print("----- Welcome to Guess Number Game! -----")
        print(": ̗̀➛ Enter the numbers you want to guess!")
        numberGuessGame.numberGuess_game(user)
        isagain = playAgain()

    elif choose == "3":
        print("-" * 25)
        print()
        print("This is Leader board. Please check your score!")
        scoreGames()
        isagain = playAgain()

    elif choose == "0":
        print("EXIT ....")
        isagain = False
        break

    else:
        print("Sorry. Please choose again")
        print("LOADING ....")


