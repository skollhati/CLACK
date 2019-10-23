from . import app, render_template, request


@app.route('/')
def index():
    return render_template('index/index_contents.html')
