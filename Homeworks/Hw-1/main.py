from flask import Flask

from utils import show_requirements, show_space

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <p>Hello, Dima</p>
    <a href='/requirements/'>/requirements/</a><br>
    <a href='/generate-users/'>/generate-users/</a><br>
    <a href='/mean/'>/mean/</a><br>
    <a href='/space/'>/space/</a>
    """


@app.route('/requirements/')
def requirements():
    return show_requirements()


@app.route('/generate-users/')
def users():
    pass


@app.route('/mean/')
def mean():
    pass


@app.route('/space/')
def space():
    return show_space()


if __name__ == '__main__':
    app.run(debug=True)
