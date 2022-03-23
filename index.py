import platform

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='World'):
    version = platform.python_version()
    return 'Hello {} from Python v{}'.format(name, version)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
