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
    <p>Here’s what we’ve done:</p>
    <ul>
      <li>Deployed the app from GitHub to AWS Elastic Beanstalk</li>
      <li>Set up automatic deployment with GitHub Actions</li>
      <li>Fixed all issues so the app runs smoothly</li>
      <li>Made sure the app no longer shows errors</li>
    </ul>
    <p>Thanks for checking in!</p>
    """
    return render_template_string(message)

if __name__ == '__main__':
    application.run(debug=True)

