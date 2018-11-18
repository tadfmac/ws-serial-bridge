import board
import digitalio
import time
import supervisor

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

sleepTime = 0.5
while True :
	if(supervisor.runtime.serial_bytes_available):
		input_data = input()
		input_time = float(input_data);
		if(input_time >= 0.01 and input_time <= 1.0):
			sleepTime = input_time
	led.value = True
	time.sleep(sleepTime)
	led.value = False
	time.sleep(sleepTime)
