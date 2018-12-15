# Move your board around to see the values change.
# Open the plotter in Mu to see the values on a graph!
import time
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print((x, y, z))
    time.sleep(0.5)
