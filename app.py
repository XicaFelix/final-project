from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

contacts = [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html', contacts=contacts)

@app.route('/stress_check', methods=['GET', 'POST'])
def stress_check():
    if request.method == 'POST':
        stress_level = int(request.form['stressLevel'])
        # Redirect to high stress walkthrough if level > 60
        if stress_level > 60:
            return redirect(url_for('high_stress'))
        # Redirect to dashboard if stress level is <= 60
        return redirect(url_for('dashboard')) 
    
    # If it's a GET request, display the stress check form
    return render_template('stress_walkthrough.html')

@app.route('/stress_check/pg-1', methods=['GET'])
def high_stress():
    contacts = [
        {"id": 1, "name": "Ginger Lee", "email": "ginger.ale@example.com"},
        {"id": 2, "name": "Yoland Vega", "email": "yolanda@example.com"},
        {"id": 3, "name": "Charlie Chaplin", "email": "charlie@example.com"}
        ]
    
    return render_template('high_stress_walkthrough.html', contacts=contacts)

@app.route('/stress_check/pg-2', methods=['GET'])
def high_stress_pg2():
    return render_template('high_stress_walkthrough_pg2.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
