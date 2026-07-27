import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
@app.route('/')
def home():
    return render_template('index.html')

# Example API or Route for dosage calculation/reminders if needed
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    # Add your logic here
    return jsonify({"status": "success", "message": "Calculated successfully"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
