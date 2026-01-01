from machine import ADC, Pin
import time

# Left sensor on pin 26, right sensor on pin 27
adc26 = ADC(Pin(26))
adc27 = ADC(Pin(27))

print("Dioode Sensor Test")

while True:
    val26 = adc26.read_u16()
    val27 = adc27.read_u16()
    
    # Calculate percentage difference
    maxval = max(val26, val27)
    if maxval == 0:
        diff_percent = 0
    else:
        diff_percent = abs(val26 - val27) / maxval * 100
    
    # Print sensor values
    print(f"Left: {val26} | Right: {val27}", end="")
    
    # Determine which sensor is stronger
    if diff_percent > 20:
        if val26 > val27:
            stronger = "LEFT (26)"
        else:
            stronger = "RIGHT (27)"
        print(f"Stronger: {stronger}")
    else:
        print("Equal")
    
    time.sleep(0.1)