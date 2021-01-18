import warnings
import winsound
import FileHandlers as FH


def fxn():
    warnings.warn("deprecated", DeprecationWarning)


def Suppress():
    warnings.filterwarnings("ignore")


def Query_Config(header):
    f = open('config.txt', 'r')

    while True:
        line = f.readline()
        if not line:
            break

        if header in line:
            line = line.replace(header, '')  # Not clean but it works leave me alone
            return line

def Beep():
    frequency = 2500
    duration = 100
    winsound.Beep(frequency, duration)


def Build_UI():
    print("UI built")


