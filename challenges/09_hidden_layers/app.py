from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h3>Challenge 09: Hidden Layers</h3><p>Some secrets were baked and deleted in earlier layers. Can you find them?</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
