import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
items = dict()
command = ""
item = ""

while(1):
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    try:
        speechString = r.recognize_google(audio)
        parsedCommands = speechString.split(" ")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    if(len(parsedCommands) > 0):
        command = parsedCommands[0]

    if(len(parsedCommands) > 1):
        item = parsedCommands[1]

    if(command == "add"):
        if item in items:
            items[item] = str(int(items[item]) + 1)
        else:
            items[item] = str(1)

        print(item + " added")

    if(command == "remove"):
        if item in items:
            if(int(items[item]) > 1):
                items[item] = str(int(items[item]) - 1)
            else:
                try:
                    items.pop(item, None)
                except:
                    pass
        print(item + " removed")

    if(command == "display"):
        print(items)
        engine = pyttsx3.init()
        engine.say("Here's your list")
        engine.say(' '.join(items.keys()))
        engine.runAndWait()

    command = ""
    item = ""
    days = ""
    parsedCommands.clear()
