from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Live from GitHub CI/CD on Elastic Beanstalk 💥"


if __name__ == '__main__':
    app.run()
