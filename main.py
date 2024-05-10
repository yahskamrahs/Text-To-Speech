import pyttsx3
def textspeak():
    while(True):
        engine=pyttsx3.init()
        engine.setProperty('rate',150)
        engine.setProperty('volume',0.9)
        text=input("Enter a Text to Speak:")
        if(text=="q"):
            engine.say("Thank You")
            engine.runAndWait()
            break
        engine.say(text)
        engine.runAndWait()
       
textspeak()

