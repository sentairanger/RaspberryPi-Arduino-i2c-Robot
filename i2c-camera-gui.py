from guizero import PushButton, App, Window, Text
from smbus import SMBus
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from gpiozero import LED
from datetime import datetime

eye = LED(25)

# Define the new camera and the configurations
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
moment = datetime.now()

addr = 0x8
bus = SMBus(1)

def i2c_forward():
    print("1")
    bus.write_byte(addr, 0x1)

def i2c_backward():
    print("2")
    bus.write_byte(addr, 0x2)

def i2c_left():
    print("3")
    bus.write_byte(addr, 0x3)

def i2c_right():
    print("4")
    bus.write_byte(addr, 0x4)

def i2c_stop():
    print("0")
    bus.write_byte(addr, 0x0)

def record():
    print("recording!")
    eye.on()
    picam2.start_recording(encoder, '/home/torvalds/Videos/i2c_gui_video2_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    eye.off()
    print("stop recording!")
    picam2.stop_recording()

app = App(title='i2c GUI Robot', layout='grid')
app.bg = (51, 246, 255)
# Add a camera window
camera_window = Window(app, "Updated Camera Control")
camera_window.bg = (51, 246, 255)

forward_button = PushButton(app, i2c_forward, text='^', grid=[2,0])
left_button = PushButton(app, i2c_left, text='<', grid=[1,1])
stop_button = PushButton(app, i2c_stop, text='O', grid=[2,1])
right_button = PushButton(app, i2c_right, text='>', grid=[3,1])
backward_button = PushButton(app, i2c_backward, text='v', grid=[2,2])
camera_text = Text(camera_window, text="Camera Controls")
record_button = PushButton(camera_window, text="record", command=record)
record_stop = PushButton(camera_window, text="stop", command=stop_record)

forward_button.bg = "red"
forward_button.text_size = 20
backward_button.bg = "red"
backward_button.text_size = 20
left_button.bg = "red"
left_button.text_size = 20
right_button.bg = "red"
right_button.text_size = 20
stop_button.bg = "red"
stop_button.text_size = 20
# camera buttons
record_button.text_size = 20
record_button.bg = "green"
record_stop.text_size = 20
record_stop.bg = "red"
camera_text.text_size = 20
