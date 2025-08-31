# app/app.py
from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Replace in production

FLAG_DIR = os.path.join(os.path.dirname(__file__), '../flags')
CHALLENGES = {
    "01": ("Sensitive Keys in Codebase", 10001),
    "02": ("Docker-in-Docker Exploitation", 10002),
    "03": ("SSRF in Kubernetes", 10003),
    "04": ("Container Escape", 10004),
    "05": ("Docker CIS Benchmark Violations", 10005),
    "06": ("Kubernetes CIS Benchmark Violations", 10006),
    "07": ("Attacking Private Registry", 10007),
    "08": ("NodePort Exposed Services", 10008),
    "09": ("RBAC Misconfiguration", 10009),
    "10": ("Falco Runtime Detection Bypass", 10010)
}

flags = {}
for num, (name, _) in CHALLENGES.items():
    filename = f"{num}_{name.lower().replace(' ', '_')}.txt"
    try:
        with open(os.path.join(FLAG_DIR, filename)) as f:
            flags[num] = f.read().strip()
    except FileNotFoundError:
        flags[num] = "FLAG{not-set}"

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', challenges=CHALLENGES)

@app.route('/challenges', methods=['GET', 'POST'])
def challenge_page():
    if 'status' not in session:
        session['status'] = {num: 'Unsolved' for num in CHALLENGES}

    # Copy to local variable and update only what's submitted
    status = session['status']

    if request.method == 'POST':
        challenge_id = request.form['challenge_id']
        submitted_flag = request.form['flag'].strip()
        if submitted_flag == flags.get(challenge_id):
            status[challenge_id] = '✅ Correct'
        else:
            status[challenge_id] = '❌ Wrong'
        session['status'] = status  # Save back to session

    # Compute solved count
    solved_count = sum(1 for val in status.values() if val == '✅ Correct')

    return render_template(
        'challenges.html',
        challenges=CHALLENGES,
        status=status,
        solved_count=solved_count
    )
@app.route('/reset', methods=['GET'])
def reset():
    session.clear()
    return redirect(url_for('challenge_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
