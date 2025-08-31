from flask import Flask

app = Flask(__name__)


API_SECRET = "FLAG{hardcoded_api_key_1}"

@app.route('/')
def index():
    return f"""
    <h3>Challenge 01: Sensitive Keys in Codebase</h3>
    <p>This service uses a third-party API. Look closer at the source code or decompile the image!</p>
    <p>Status: Online</p>
    """
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
