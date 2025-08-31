import subprocess
try:
    import flask
except ImportError:
    subprocess.check_call(["pip", "install", "flask"])
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🏴 Docker CIS Violation Challenge: This container violates best practices!"

@app.route("/whoami")
def whoami():
    return os.popen("whoami").read()

@app.route("/badfilepermissions")
def perms():
    return "This container runs as root, exposing sensitive config."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10005)
