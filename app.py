from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graphs')
def graphs():
    return render_template('Assignment1Graph.html')

app.run()