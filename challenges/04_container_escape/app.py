from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h3>Challenge 04: Container Escape</h3>
    <p>This container is running in <b>privileged</b> mode and has host volume mounted.</p>
    <p>Try to escape the container and read <code>/mnt/host_root/flag_escape.txt</code>.</p>
    """

@app.route('/hint')
def hint():
    return "Try checking /mnt/host_root/ from within the container shell."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
