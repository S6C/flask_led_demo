from flask import Flask, request, render_template
import json


def ledControl(status):
    if status == True:
        print("LED ON")
    else:
        print("LED OFF")


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
        return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
