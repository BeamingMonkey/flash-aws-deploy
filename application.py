from flask import Flask
application = Flask(__name__)  # Required name for AWS Elastic Beanstalk

@application.route('/')
def hello():
    return "Live from GitHub CI/CD on Elastic Beanstalk 💥"

if __name__ == '__main__':
    application.run()
