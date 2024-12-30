from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.now())

if __name__ == '__main__':
    app.run()