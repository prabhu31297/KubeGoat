from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Challenge 07: Attacking Private Docker Registry</h2><p>Try inspecting Docker metadata or explore common private registry misconfigs.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
