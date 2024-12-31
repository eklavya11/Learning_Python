secret_word = "eklavya"

guess = ""
count =0
while(guess!=secret_word and count<3):
    guess=input("Enter guess word:")
    count=count+1
    if(guess==secret_word):
        print("correct guess")



if(count==3 and guess!=secret_word):
      print("You are out of guesses")
    