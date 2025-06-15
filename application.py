from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to my Flask app!</h1>
    <a href="/success">Click here to see deployment success message</a>
    '''

@app.route('/success')
def success():
    message = """
    <h2>🔥 Yes, Arun — your app is LIVE and running from GitHub CI/CD on Elastic Beanstalk! 💥</h2>
    <p>✅ What You Just Achieved:</p>
    <ul>
      <li>Deployed a Flask app from GitHub to AWS Elastic Beanstalk</li>
      <li>Set up a CI/CD pipeline using GitHub Actions</li>
      <li>Fixed the Procfile issue and made the application.py run correctly</li>
      <li>Resolved 502 Bad Gateway errors</li>
    </ul>
    """
    return render_template_string(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
