from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<p>Home page</p>"


@app.route('/config_video')
def conf():
    return "<h1>config</h1><p>salut</p>"


app.run(debug=True)