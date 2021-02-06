import socket
from threading import Thread


def main():
    print("[+] Connecting to master.")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.2",7777))
    print("[+] Connected to master")
    while True:
        msg = s.recv(1024).decode()
        print("[+] Master said: ", msg)
        if msg == "exit":
            break



if __name__=="__main__":
    main()