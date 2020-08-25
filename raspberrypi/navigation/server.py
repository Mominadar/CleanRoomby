from flask import Flask,Response,render_template
import json
from flask_socketio import SocketIO, send ,emit
from flask import Flask,Response,render_template
import json
from flask_socketio import SocketIO, send ,emit
import time
import threading
import argparse
import datetime
import imutils
import RPi.GPIO as gpio

outputFrame = None
lock = threading.Lock()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

import time
import threading
import argparse
import datetime
import imutils
import RPi.GPIO as gpio

outputFrame = None
lock = threading.Lock()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
   
time.sleep(0.1)



def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(27, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)

def forward(sec):
 init()
 print("forward move")
 gpio.output(17, True)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 gpio.cleanup()

def right(sec):
 init()
 print("right move")
 gpio.output(17, True)
 gpio.output(27, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()

def left(sec):
 init()
 print("left move")
 gpio.output(17, False)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 gpio.cleanup()
 
def reverse(sec):
 init()
 print("back move")

 gpio.output(17, False)
 gpio.output(27, True)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()
 

 
def stop(sec):
 init()
 print("stop move")

 gpio.output(17, False)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()
 
 
@app.route('/')
def index():
    return render_template('index.html')

############################connect#######
@socketio.on('connect')
def test_connect():
    print("ggg")
    emit('connection_response','Connection established')
    @socketio.on ('connection')
    def on_connection(c_res):
        print("connection made")
        print(c_res)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

##########Controller Control ###############
    
@socketio.on('forward_con')
def on_forward_con(*args):
    print("forward")
    forward(0.5)
    #print(args[0],str(args[1]))


@socketio.on('right_con')
def on_right_con(*args):
    print("right")
    right(0.5)
    #print(args[0])


@socketio.on('left_con')
def on_left_con(*args):
    print("left")
    left(0.5)
    #print(args[0])

@socketio.on('back_con')
def on_back_con(*args):
    print("back")
    reverse(0.5)
    #print(args[0])

@socketio.on('stop_con')
def on_stop_con(*args):
    print("stop")
    stop(0.5)
    #print(args[0])
"""    
@socketio.on('slow_gait_con')
def on_left_con(*args):
    print(args[0])

@socketio.on('fast_gait_con')
def on_back_con(*args):
    print(args[0])

##################Rotate Body ###########################
@socketio.on('zero_con')
def on_zero_con(*args):
    print(args[0])


@socketio.on('fortyfive_con')
def on_fortyfive_con(*args):
    print(args[0])


@socketio.on('ninty_con')
def on_ninty_con(*args):
    print(args[0])

@socketio.on('onethirtyfive_con')
def on_onethirtyfive_con(*args):
    print(args[0])

@socketio.on('oneeighty_con')
def on_oneeighty_con(*args):
    print(args[0])

@socketio.on('twotwentyfive_con')
def on_twotwentyfive_con(*args):
    print(args[0])


@socketio.on('twoseventy_con')
def on_twoseventy_con(*args):
    print(args[0])

@socketio.on('threesixty_con')
def on_threesixty_con(*args):
    print(args[0])

##############################Move Body Panel######################
@socketio.on('Y_left_con')
def on_Y_left_con(*args):
    print(args[0])

@socketio.on('Y_right_con')
def on_Y_right_con(*args):
    print(args[0])

@socketio.on('pitch_up_con')
def on_pitch_up_con(*args):
    print(args[0])


@socketio.on('pitch_low_con')
def on_pitch_low_con(*args):
    print(args[0])

@socketio.on('default_pitch_con')
def on_default_pitch_con(*args):
    print(args[0])

@socketio.on('roll_right_con')
def on_roll_right_con(*args):
    print(args[0])

@socketio.on('roll_left_con')
def on_roll_left_con(*args):
    print(args[0])


##################################Adjust Height Panel###############

@socketio.on('max_con')
def on_max_con(*args):
    print(args[0])

@socketio.on('maxMedium_con')
def on_maxMedium_con(*args):
    print(args[0])

@socketio.on('default_con')
def on_default_con(*args):
    print(args[0])

@socketio.on('min_con')
def on_min_con(*args):
    print(args[0])

@socketio.on('minMedium_con')
def on_minMedium_con(*args):
    print(args[0])
"""

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5090)
