from flask import Flask

app = Flask(__name__)

@app.route('/data')
def get_data():
    return 'This DATA is from the Backend Server!'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)