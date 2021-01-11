import socket

print("[+] Connecting to master.")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.10",7777))
while True:
    msg = s.recv(1024).decode()
    print("[+] Master said: ", msg)
    if msg == "exit":
        break