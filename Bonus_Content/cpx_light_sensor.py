# Shine a light on the board to see the value change.
# Open the Plotter in Mu to see the values on a graph!
import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Light level:", cpx.light)
    print((cpx.light,))
    time.sleep(1)
