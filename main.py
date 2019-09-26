from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index/index_contents.html')

@app.route('/auth/signin')
def signin():
    pass

@app.route('/auth/signup')
def signup():
    pass

@app.route('/auth/check')
def check_user():
    pass

@app.route('/auth/exist')
def exist_user():
    pass

@app.route('/main')
def main():
    return render_template('main/main_direct_message.html')

@app.route('/main/direct-message/<target>')
def direct_message(target):
    pass

@app.route('/main/channels/<channel_name>')
def channel(channel_name):
    pass

