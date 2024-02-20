#DR
you = "today"

if you == "":
    robot_brain = "I can't hear you, try again"
elif you == "hello":
    robot_brain = "Hello huhu"
elif you == "today":
    robot_brain = "thu 6"
else:
    robot_brain = "I'm fine thank you"

print(robot_brain)

import pyttsx3

robot_brain = "Hello"
robot_brain = pyttsx3.init()
robot_brain.say(robot_brain)
robot_brain.runAndWait()

import speech_recognition
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    audio = robot_ear.listen(mic)

you = robot_ear.recognize_google(audio)

print(you)

