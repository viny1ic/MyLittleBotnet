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

def main():
    print("[+] Master bot listening for incoming connections")
    for i in range(max_bots):
        thread = Thread(target=listen,args=(i+initial_port,), daemon=True)
        threads.append(thread)
        thread.start()
    while True:
        if len(slaves)!=0:
            print("[+] Enumerating all slaves.")
            for index, individual_slave in enumerate(slaves):
                print("[i] ", index, ". slave ip: ", individual_slave.getpeername())
            while True:
                msg = input("[+] enter message: ")
                for slave in slaves:
                    slave.send(msg.encode())
                if msg == "exit":
                    break
            if msg == "exit":
                break


if __name__=="__main__":
    main()