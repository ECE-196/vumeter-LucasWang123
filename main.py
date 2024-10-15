import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep


microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, 
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT


while True:
    volume = microphone.value

    num_leds = int((volume - 10000)/2730)
    '''
    volume = microphone.value

    print(volume)

    leds[0].value = not leds[0].value
    leds[1].value = not leds[0].value

    sleep(1)
    '''
    print("volume: ", volume)
    #print("led value: ", leds[0].value)
    if num_leds > 11:
        num_leds = 11
    print("number of leds to be lit: ", num_leds)
    for i in range(0, num_leds):
        leds[i].value = True
    sleep(0.2)
    for i in range(0,11):
        leds[i].value = False
    sleep(0.2)