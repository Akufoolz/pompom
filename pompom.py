from sys import argv
from tqdm import tqdm
from time import sleep
from pymsgbox import alert

def interval(num, desc):
    for _ in tqdm(range(int(num) * 60), desc=str(desc)):
        sleep(1)
    alert('{} has completed!'.format(desc), '{} Alert'.format(desc))

def getArgs():
    argsList = argv
    return argsList

def pomodoro(args):
    args = getArgs()
    try:
        for _ in range(int(args[3])):
            interval(args[1], args[4])
            interval(args[2], "Break")
    except ValueError:
        print("Please provide whole numbers for the interval lengths.")
        return 

def main():
    pomodoro(getArgs())

if __name__ == "__main__":
    main()