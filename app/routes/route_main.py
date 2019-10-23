from . import app, render_template, request

@app.route('/main')
def main():
    return render_template('main/main_direct_message.html')


@app.route('/main/direct-message/<target>')
def direct_message(target):
    pass


@app.route('/main/channels/<channel_name>')
def channel(channel_name):
    pass