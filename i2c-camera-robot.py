import pygame
from smbus import SMBus
from gpiozero import LED
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from datetime import datetime

eye = LED(25)

addr = 0x8
bus = SMBus(1)

# Define the new camera and the configurations
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
moment = datetime.now()

# Blink eye 2 times to ensure the code is running correctly
eye.blink(n=2)

#Define the record and stop_record functions
def record():
    print("recording!")
    eye.on()
    picam2.start_recording(encoder, '/home/torvalds/Videos/i2c_video2_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    eye.off()
    print("stop recording!")
    picam2.stop_recording()

#We must open a Pygame window to allow it to detect user events
screen = pygame.display.set_mode([240, 160])

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				  print('Right')
				  bus.write_byte(addr, 0x4)
			if event.key == pygame.K_LEFT:
				  print('Left')
				  bus.write_byte(addr, 0x3)
			if event.key == pygame.K_UP:
				  print('Up')
				  bus.write_byte(addr, 0x1)
			if event.key == pygame.K_DOWN:
		      print('Down')
				  bus.write_byte(addr, 0x2)
			if event.key == pygame.K_t:
			    print('stop')
			    bus.write_byte(addr, 0x0)
      if event.key == pygame.K_r:
          record()
      if event.key == pygame.K_s:
          stop_record()
			if event.key == pygame.K_q:
		      pygame.quit()
