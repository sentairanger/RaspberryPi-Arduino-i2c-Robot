from guizero import PushButton, App
from smbus import SMBus

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

app = App(title='i2c GUI Robot', layout='grid')
app.bg = (51, 246, 255)

forward_button = PushButton(app, i2c_forward, text='^', grid=[2,0])
left_button = PushButton(app, i2c_left, text='<', grid=[1,1])
stop_button = PushButton(app, i2c_stop, text='O', grid=[2,1])
right_button = PushButton(app, i2c_right, text='>', grid=[3,1])
backward_button = PushButton(app, i2c_backward, text='v', grid=[2,2])

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

app.display()
