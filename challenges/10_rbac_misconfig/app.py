from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    role = request.args.get('role', 'guest')
    if role == 'admin':
        return "Welcome admin! FLAG{rbac_misconfig_root_access}"
    return "Access denied. Try harder."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
