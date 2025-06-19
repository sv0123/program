# File: app/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    # Added "on Windows!" for clarity
    return "Hello from Microservice App on Windows!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)