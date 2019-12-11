from flask import Flask, render_template, request

app = Flask(__name__)


# Routes
@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
