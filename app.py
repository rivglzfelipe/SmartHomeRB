import RPi.GPIO as gpio
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return  'hello world'

@app.route('/node/<gp>/<do>')
def lightRoom(gp,do):
  gpio.setmode(gpio.BOARD)
  gpio.setup(11, gpio.OUT)
  gpio.setup(13, gpio.OUT)
  if do == 'off':
    gpio.output(int(gp), True)
    return 'luz apagada'
  if do == 'on':
    gpio.output(int(gp), False)
    return 'luz prendida'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')


