import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Live from GitHub CI/CD on Elastic Beanstalk 💥"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # EB sets this env variable
    app.run(host='0.0.0.0', port=port)
