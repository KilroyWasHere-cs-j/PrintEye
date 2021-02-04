import winsound
import FileHandlers as FH
import pyttsx3
import OID
from datetime import *
import Messager as M
import sys
import os


def Query_Config(header):
    try:
        cPath = GDN()
        path = 'config.txt'
        f = open(path, 'r')

        while True:
            line = f.readline()
            if not line:
                break

            if header in line:
                line = line.replace(header, '')  # Not clean but it works leave me alone
                return line
    except:
        print("No email")


def Beep():
    frequency = 2500
    duration = 100
    winsound.Beep(frequency, duration)


def Beep_Custom(duration, times):
    frequency = 2500
    t = 0
    while t != times:
        t = t + 1
        winsound.Beep(frequency, duration)


def Speak(mes):
    engine = pyttsx3.init()
    engine.say(mes)
    engine.runAndWait()


def Print_Failure():
    Warning()
    FH.Update_Log("Print Failure detected")
    M.Send_Email("Failure at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    decision = input("Do you wish to continue print monitoring? True/False: ")
    if decision == "True":
        print("Attempting to continue")
        OID.Process(camera=0)
    elif decision == "False":
        print("Stopping print monitoring, and closing app")
        FH.Update_Log("Closing app")
        sys.exit(0)


def Build_UI():
    # This is pointless
    print("UI built")


def GDN():
    return os.getcwd()

