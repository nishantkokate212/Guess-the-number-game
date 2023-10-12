import random
import pyttsx3

num=random.randint(1,100)
guessNo=0
userGuess=None

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Game Started... user,please guess the number?")
while num!=userGuess:
    
    try:
        userGuess=int(input("Guess the number: "))
        guessNo+=1

        if userGuess==num:
            print("You guessed Right Number!")
            speak(f"Brilliant, Your guess is right!")
        
        elif userGuess<num:
            print("Please Try Bigger number!")
            speak("Please try Bigger number!")
        
        elif userGuess>num:
            print("Please Try smaller number!")
            speak("Please try smaller number!")
    except ValueError:
        print("please enter valid number in range of 1 to 100..")
        speak("please enter valid number in range of 1 to 100..")
    
print(f"you took {guessNo} guesses to guessed correct number!!")
speak(f"you took {guessNo} guesses to guessed correct number!!")
    
with open ("hiscore.txt") as a:
    hiscore=a.read()
if int(hiscore)>guessNo:
    with open ("hiscore.txt","w") as a:
        newscore=a.write(str(guessNo))

    