import socket
from AlphaBot import AlphaBot
import time

alphabot = AlphaBot()
alphabot.stop()

s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)
conn, addr = s.accept()
 
while True:
    cmd = conn.recv(1024).decode().strip()
    if cmd == "avanti":
        alphabot.forward()
        time.sleep(2)
        alphabot.stop()
    elif cmd == "indietro":
        alphabot.backward()
        time.sleep(2)
        alphabot.stop()
    elif cmd == "sinistra":
        alphabot.left()
        time.sleep(0.29)
        alphabot.stop()
    elif cmd == "destra":
        alphabot.right()
        time.sleep(0.29)
        alphabot.stop()
    elif cmd == "stop":
        alphabot.stop()
    elif cmd == "esci":
        alphabot.stop()
        break