from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    html = "<html><body>Welcome </body></html>"
    return html

@app.route('/welcome/home')
def home():
    html = "<html><body>Welcome Home </body></html>"
    return html

@app.route('/welcome/back')
def back():
    html = "<html><body>Welcome Back</body></html>"
    return html


