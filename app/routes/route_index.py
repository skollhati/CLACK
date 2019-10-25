from . import app, render_template, request, session


@app.route('/')
def index():

    return render_template('index/index_contents.html')
