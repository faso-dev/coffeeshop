from src.api import app


def __main__():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    __main__()
