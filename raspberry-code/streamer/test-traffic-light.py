from gpiozero import LED
import time

# Assign LEDs to GPIO pins (BCM numbering)
RED = LED(17)
YELLOW = LED(27)
GREEN = LED(22)

print("Starting traffic light test. Press Ctrl+C to exit.")

try:
    while True:
        print("RED ON")
        RED.on()
        YELLOW.off()
        GREEN.off()
        time.sleep(2)

        print("YELLOW ON")
        RED.off()
        YELLOW.on()
        GREEN.off()
        time.sleep(2)

        print("GREEN ON")
        RED.off()
        YELLOW.off()
        GREEN.on()
        time.sleep(2)
except KeyboardInterrupt:
    print("\nTest interrupted. Turning off all lights.")
    RED.off()
    YELLOW.off()
    GREEN.off()
