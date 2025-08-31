from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h3>Challenge 08: NodePort Exposed Service</h3><p>Simulates a backend mistakenly exposed to the internet on a high port.</p>"

@app.route('/admin')
def admin():
    auth = request.args.get('auth', '')
    if auth == 'superadmin':
        return "Access granted. FLAG{nodeport_exposure_leak}"
    return "403 Forbidden"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
