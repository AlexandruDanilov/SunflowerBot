from machine import Pin, PWM, ADC
import time

adc_left = ADC(Pin(26))
adc_right = ADC(Pin(27))

servo = PWM(Pin(3))
servo.freq(50)

START_ANGLE = 90
MOVE_SPEED = 5
TOLERANCE_PERCENT = 15
DARK_THRESHOLD = 2500

current_angle = START_ANGLE

def set_angle(angle):
    duty = int((angle / 180.0 * 6553) + 1638)
    if duty < 1000: duty = 1000
    if duty > 9000: duty = 9000
    servo.duty_u16(duty)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

print("START")
set_angle(current_angle)
time.sleep(2)

while True:
    val_left = adc_left.read_u16()
    val_right = adc_right.read_u16()
    maximum = max(val_left, val_right)
    if maximum == 0:
        diff_percent = 0
    else:
        diff = abs(val_left - val_right)
        diff_percent = (diff / maximum) * 100

    print(f"L:{val_left} R:{val_right} D:{diff_percent:.1f} A:{current_angle}", end=" ")

    if val_left < DARK_THRESHOLD and val_right < DARK_THRESHOLD:
        print("IDLE")
    elif diff_percent <= TOLERANCE_PERCENT:
        print("STOP")
    else:
        if val_left > val_right:
            print("L")
            current_angle += MOVE_SPEED
        else:
            print("R")
            current_angle -= MOVE_SPEED
        current_angle = clamp(current_angle, 0, 180)
        set_angle(current_angle)

    time.sleep(0.05)
