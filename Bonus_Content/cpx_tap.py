# Open the serial console and double-tap your board to see a print statement!
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 2

while True:
    if cpx.tapped:
        print("Tap detected!")
