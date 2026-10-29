from AlphaBot import AlphaBot
import time

alphabot = AlphaBot()

for i in range(4):
    alphabot.forward()
    time.sleep(1)
    alphabot.left()
    time.sleep(0.29)
alphabot.stop()
