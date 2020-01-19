from flask import Flask, request, render_template
import json
from sense_hat import SenseHat
sense = SenseHat()

def ledControl(status):
    if status == True:
        print("LED ON")
    else:
        print("LED OFF")


def senseControl(status):
    X = [255, 255, 255]  # On
    O = [0, 0, 0]  # Off

    off = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]

    on = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
    ]

    if status == True:
        sense.set_pixels(on)
    if status == False:
        sense.set_pixels(off)
    else:
        print('Error setting pixels')  

app = Flask(__name__)

led = True


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/lights/led', methods=['GET', 'POST'])
def ledStatus():
    global led
    if request.method == 'GET':
        return json.dumps({"led": led})
    if request.method == 'POST':
        data = request.get_json()
        led = data['led']
        ledControl(led)
        senseControl(led)
        return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
