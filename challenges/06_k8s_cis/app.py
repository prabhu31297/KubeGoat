from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h3>Challenge 06: K8s CIS Misconfiguration</h3>
    <p>Audit logs and sensitive configs might be exposed.</p>
    <a href='/config'>Download kubelet config</a>
    """

@app.route('/config')
def config():
    return send_file('/app/kubelet.conf', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
