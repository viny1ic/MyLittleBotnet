from threading import Thread

def printA():
    while True:
        print("a")

def printB():
    while True:
        print("b")

Thread(target=printA).start()
Thread(target=printB).start()
