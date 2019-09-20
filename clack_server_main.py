from flask import Flask, app, render_template

app = Flask(__name__)


@app.route("/")
def html_test():
    return render_template("main_element/main_contents.html")



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)