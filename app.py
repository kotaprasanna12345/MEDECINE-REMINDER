from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate-dosage', methods=['POST'])
def calculate_dosage():
    """Educational dosage calculation API endpoint with safety validation."""
    data = request.json
    try:
        age = float(data.get('age', 0))
        weight = float(data.get('weight', 0))
        dose_per_kg = float(data.get('dosePerKg', 2))
        num_doses = int(data.get('numDoses', 2))

        # Basic Educational Safety Checks
        if weight <= 0 or weight > 300:
            return jsonify({
                'success': False,
                'message': 'Please enter a valid weight between 1 kg and 300 kg for educational demonstration.'
            })

        if age < 0 or age > 120:
            return jsonify({
                'success': False,
                'message': 'Please enter a valid age between 0 and 120 years.'
            })

        # Formula Calculation
        daily_dose = weight * dose_per_kg
        dose_per_admin = daily_dose / num_doses

        return jsonify({
            'success': True,
            'dailyDose': round(daily_dose, 2),
            'dosePerAdmin': round(dose_per_admin, 2),
            'message': 'Input values are valid for educational demonstration.'
        })

    except Exception as e:
        return jsonify({'success': False, 'message': f'Invalid input data: {str(e)}'})

if __name__ == '__main__':
    print("Starting Medicine Reminder & Dosage Calculator Server...")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)