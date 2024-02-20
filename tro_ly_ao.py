import speech_recognition
import pyttsx3
from datetime import date

while True:
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot_brain = ""
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you == "i can't hear you"

    print("You: " + you)


    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello nho"
    elif "today" in you:

        today = date.today()
        # Textual month, day and year
        robot_brain = today.strftime("%B %d, %Y")
        print(robot_brain)
    elif "bye" in you:
        robot_brain = "Bai, chu chu"
        print("Robot: " + robot_brain)

        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you"
    print("Robot: " + robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()