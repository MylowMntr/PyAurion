from flask_ngrok import run_with_ngrok
from flask import Flask, session  # Import the Flask class

app = Flask(__name__)    # Create an instance of the class for our use
run_with_ngrok(app)


app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == "__main__":
    app.run()