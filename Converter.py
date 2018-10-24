import speech_recognition as sp

s = sp.Recognizer()

with sp.Microphone() as input_source:
    print("Say somethings:")
    audio = s.listen(input_source)

    try:
        text = s.recognize_google(audio)
        print("You said : {}".format(text))


    except:
        print("Voice error")

