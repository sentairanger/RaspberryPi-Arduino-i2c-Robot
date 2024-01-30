from flask import Flask, render_template, request
from smbus import SMBus

addr = 0x8
bus = SMBus(1)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/forward')
def forward():
    print("1")
    bus.write_byte(addr, 0x1)
    return render_template("index.html")

@app.route('/backward')
def backward():
    print("2")
    bus.write_byte(addr, 0x2)
    return render_template("index.html")

@app.route('/left')
def left():
    print("3")
    bus.write_byte(addr, 0x3)
    return render_template("index.html")

@app.route('/right')
def right():
    print("4")
    bus.write_byte(addr, 0x4)
    return render_template("index.html")

@app.route('/stop')
def stop():
    print("0")
    bus.write_byte(addr, 0x0)
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')