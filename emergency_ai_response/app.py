from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    age = request.form['age']
    symptoms = request.form['symptoms']
    duration = request.form['duration']

    # Mock AI responses (you can connect actual AI model or DB here)
    hospitals = [
        {
            'name': 'UrbanCare Hospital',
            'distance': '32 km',
            'doctors_available': 'Yes',
            'ambulance_time': '1.2 hours',
            'facilities': ['Cardiology', 'Oxygen Bed', 'ICU']
        },
        {
            'name': 'Greenway Medical Center',
            'distance': '25 km',
            'doctors_available': 'Yes',
            'ambulance_time': '0.9 hours',
            'facilities': ['Chest Pain Specialist', 'Portable Ventilator']
        },
        {
            'name': 'Rural Health Camp',
            'distance': '15 km (Midpoint)',
            'doctors_available': 'Limited',
            'ambulance_time': '0.6 hours',
            'facilities': ['First Aid', 'Basic Monitoring']
        }
    ]

    return render_template('result.html', age=age, symptoms=symptoms, duration=duration, hospitals=hospitals)

if __name__ == '__main__':
    app.run(debug=True)

