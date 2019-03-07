from flask import Flask, render_template
from flask_socketio import SocketIO, send
import I2C_LCD_driver
from time import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
mylcd = I2C_LCD_driver.lcd()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('mensaje')
def handleMessage(msg):
    print('mensaje: ' + msg)
    mylcd.lcd_display_string("                ", 1)
    mylcd.lcd_display_string(msg, 1)

if __name__ == '__main__':
    #socketio.run(app,debug=True)
    app.run(debug=True,host='0.0.0.0',port=4500)

