from machine import PWM
from time import sleep
import machine
# Initialize PWM on GPIO pin 15
pwm_pin = PWM(15,freq=1000, duty_u16=32768)
# Initialize PWM on GPIO pin 16
pwm_pin1 = PWM(16,freq=1000, duty_u16=16384)

while True:
    choice=int(input("valg 1 (højre) eller 2 (venstre): "))
    if choice==1: #dreje motor til højre
        pwm_pin.init()
        sleep(3)
    else: #dreje motor til venstre
        pwm_pin1.init()
        sleep(3)
    
    
    
    
    
    
    
    #pass
