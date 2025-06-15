from flask import Flask, render_template_string

application = Flask(__name__)

@application.route('/')
def home():
    return '''
    <h1>Welcome to Arunraj's Flask App!</h1>
    <p><a href="/success">Click here to see deployment status</a></p>
    '''

@application.route('/success')
def success():
    message = """
    <h2>🎉  app is LIVE and working perfectly! 🚀</h2>
    <p>Here’s what’s been successfully done using CI/CD:</p>
    <ul>
      <li>✅ Deployed the app from <strong>GitHub</strong> to <strong>AWS Elastic Beanstalk</strong></li>
      <li>🔁 Set up <strong>automatic CI/CD</strong> pipeline using <strong>GitHub Actions</strong></li>
      <li>🛠️ Fixed all configuration and deployment issues</li>
      <li>🔒 No more 502 or startup errors — app runs smoothly now</li>
      <li>📦 Future updates from GitHub will deploy automatically</li>
    </ul>
    <p>Thanks for checking in!</p>
    """
    return render_template_string(message)

if __name__ == '__main__':
    application.run(debug=True)

