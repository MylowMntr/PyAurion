from flask import Flask  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)