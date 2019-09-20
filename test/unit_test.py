import unittest
from flask import Flask, app, render_template

app = Flask(__name__)


@app.route("/")
def html_test():
    return render_template("index/../templates/layout.html")
    # return "test"
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.run(host="127.0.0.1")



    def test_something(self):
        # self.assertEqual(True, False)
        pass

if __name__ == '__main__':

    unittest.main()
