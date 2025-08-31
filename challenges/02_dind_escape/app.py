from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Docker Exploitation Lab</h1>
    <p>This container is misconfigured to allow Docker commands inside!</p>
    <p>Try to find the FLAG stored in a Docker volume or container.</p>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
