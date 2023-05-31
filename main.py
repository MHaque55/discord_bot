from flask import Flask
import datetime

current_datetime = datetime.datetime.now()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return (f'Current time = {current_datetime}')

if __name__ == '__main__':
    app.run(port=5555)