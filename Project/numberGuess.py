import random

class Guessing:
  global score
  def numberGuess_game(user_name):
    score = 100
    guess_number = random.randrange(1, 11)
    num_of_tries = 5
    print("Guess number between [ 1 - 10 ]")
    print("Number of tries is %d." % num_of_tries)
    print()

    while num_of_tries >= 1:
      answer = int(input("What's your guess number : ")) 
      if answer == guess_number:
        print("----------------------------------------")
        print("Congratulations!. You are very genius ,How did you know?")
        break

      elif answer != guess_number:
        print("❀  You have %d more chance left.  ❀" % (num_of_tries - 1))
        num_of_tries -= 1
        score -= 20

        if num_of_tries == 0:
          print("----------------------------------------")
          print("Unfortunately, but you guessed too much. You lost.")
          break

        elif answer > guess_number :
          print("Number is too high! Try lower Number.")
          print()

        elif answer < guess_number :
          print("Number is too low! Try higher Number.")
          print()

    #print(score)
    user = user_name
    score = str(score)
    with open('data_numguess.txt', 'a', encoding='utf8') as sc:
      sc.write("\n")
      sc.write(user + "  :  " + str(score) + "   point")

    print(">>> Your score <<<")
    print(user, " : ", int(score), "  point")
      
#guess = Guessing
#user_name = "เด็กดี"
#guess.numberGuess_game(user_name)

#numberGuess_game()