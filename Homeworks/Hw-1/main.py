
from flask import Flask, request

from utils import show_requirements, show_space, show_generate_users

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
    length = request.args.get('length', '10')

    if length.isdigit():
        length = int(length)
        maximum_length = 200

        if length > maximum_length:
            return f"Length should be less than {maximum_length}"
    else:
        return f'Invalid length value "{length}"'

    return show_generate_users(length)


@app.route('/mean/')
def mean():
    pass


@app.route('/space/')
def space():
    return show_space()


if __name__ == '__main__':
    app.run(debug=True)
