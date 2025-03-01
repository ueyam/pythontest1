from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    from datetime import datetime

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Hello, World! Current time: {current_time}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
