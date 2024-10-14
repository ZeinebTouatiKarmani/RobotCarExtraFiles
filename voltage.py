from machine import Pin, ADC

# Setup the voltage measurement
battery_pin = ADC(Pin(26))

def voltage_calculation():
    adc_value = battery_pin.read_u16()
    voltage = (adc_value / 65535) * 3.3
    return voltage

