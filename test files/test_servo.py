from machine import Pin, PWM
import time

# Servomotor pwm pin is set to pin GP3, hardware pin no 5
servo = PWM(Pin(3)) 
servo.freq(50)

def set_angle(angle):
    # Calculate servo duty cycle for MG995 servomotor
    duty = int((angle / 180.0 * 6553) + 1638)
    
    # Cap servomotor limits
    if duty < 1000: duty = 1000
    if duty > 9000: duty = 9000
    
    servo.duty_u16(duty)

print("Test MG995")

while True:
    print("max left")
    set_angle(0)
    time.sleep(1)
    
    print("center")
    set_angle(90)
    time.sleep(1)
    
    print("max right")
    set_angle(180)
    time.sleep(1)