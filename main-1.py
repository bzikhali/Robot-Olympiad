import machine
import utime

# Set up GPIO pins for LEDs, MQ2 gas sensor, and PIR motion sensor
led_safe = machine.Pin(5, machine.Pin.OUT)  # Hazardous gas level LED
led_hazard = machine.Pin(2, machine.Pin.OUT)  # Safe gas level LED
led_power = machine.Pin(28, machine.Pin.OUT)  # LED off

mq2 = machine.ADC(1)  # MQ2 gas sensor analog input
pir = machine.Pin(19, machine.Pin.IN)  # PIR motion sensor input

#motion_check_int = 15 #to make sure it checks after 15 seconds
#last_check = 0
led_safe.off()
led_hazard.off()
led_power.off()

while True:
       
     # Read PIR motion sensor
    if pir.value():
            # Read MQ2 gas sensor
        led_power.on()
        print('Motion_detected')
        gas_level = mq2.read_u16()
        if gas_level > 400:  # Adjust threshold value as needed
            led_safe.on()
            led_hazard.off()
            print('safe')
            led_safe.off()
            utime.sleep(1)  # Sleep for 1 second
            led_safe.on()
        else:
            led_power.off()
            led_safe.off()
            led_hazard.on()
            print('hazard_detected')
            led_hazard.off()
            utime.sleep(1)  # Sleep for 1 second
            led_hazard.on()
        utime.sleep(15)  # Sleep for 15 second
    else:
        print('Motion_not_detected')
        led_safe.off()
        led_hazard.off()
        utime.sleep(15)  # Sleep for 15 second
