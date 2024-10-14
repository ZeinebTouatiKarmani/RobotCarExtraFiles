from machine import ADC,Pin
from time import sleep

IRSensePin = 27
IRsense = ADC(Pin(IRSensePin))

while True:
    if IRsense.read_u16() < 31775:
        print ("LOW")
    else:
        print ("HIGH")
    sleep(5)    
