from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/calculate-dosage', methods=['POST'])
def calculate_dosage():
    data = request.get_json()
    try:
        weight = float(data.get('weight', 0))
        dose_per_kg = float(data.get('dosePerKg', 0))
        num_doses = int(data.get('numDoses', 1))
        
        daily_dose = weight * dose_per_kg
        dose_per_admin = daily_dose / num_doses if num_doses > 0 else daily_dose
        
        return jsonify({
            "success": True,
            "message": "Dosage calculated successfully via Python backend rules.",
            "dailyDose": round(daily_dose, 2),
            "dosePerAdmin": round(dose_per_admin, 2)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Calculation error: {str(e)}"
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
