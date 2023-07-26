from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def getAllUsers() -> object:
    return 'All'


if __name__ == '__main__':
    app.run()


