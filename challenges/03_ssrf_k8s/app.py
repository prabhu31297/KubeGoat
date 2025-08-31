from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>SSRF Challenge</h2>
        <p>Enter a URL to fetch (simulate metadata access or internal service):</p>
        <form method="GET" action="/fetch">
            <input name="url" placeholder="http://localhost:5000/internal" size="50">
            <button type="submit">Fetch</button>
        </form>
    '''

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    try:
        res = requests.get(url, timeout=2)
        return f"<h3>Response from {url}:</h3><pre>{res.text}</pre>"
    except Exception as e:
        return f"<h3>Error:</h3><pre>{e}</pre>"

@app.route('/internal')
def internal():
    return "FLAG{ssrf_kube_service_leak}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
