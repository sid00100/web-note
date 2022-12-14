from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def form():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


app.run(debug=True)