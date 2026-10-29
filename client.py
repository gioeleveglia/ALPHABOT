import socket

s = socket.socket()
s.connect(("192.168.1.120", 5000))

while True:
    cmd = input("avanti/indietro/sinistra/destra/stop/esci > ")
    s.send(cmd.encode())
    if cmd == "esci":
        break