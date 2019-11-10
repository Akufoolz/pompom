from sys import argv
from tqdm import tqdm
from time import sleep
from playsound import playsound
from pymsgbox import alert

def interval(num, desc):
    for _ in tqdm(range(int(num) * 60), desc=desc):
        sleep(1)
    playsound('simple.wav')
    alert('{} has completed!'.format(desc), '{} Alert'.format(desc))

def getArgs():
    argsList = argv
    return argsList

def pomodoro(args):
    a = args[1]
    b = args[2]
    task = args[3]
    interval(a, task)
    interval(b, "Break")

def main():
    while True:
        pomodoro(getArgs())

if __name__ == "__main__":
    main()