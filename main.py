from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define API endpoint: POST /api/toyProductionKey


@app.route('/api/toyProductionKey', methods=['POST'])
def toy_production_key():
    # Parse JSON from request body
    data = request.get_json()

    # Validate that 'toyProductionKey' exists and is a string
    if not data or 'toyProductionKey' not in data:
        return jsonify({"error": "Missing 'toyProductionKey' in request body"}), 400

    if not isinstance(data['toyProductionKey'], str):
        return jsonify({"error": "'toyProductionKey' must be a string"}), 400

    # Extract the toyProductionKey
    toy_production_key = data['toyProductionKey']
    print(f"Received toyProductionKey: {toy_production_key}")

    # Respond with a success message
    return jsonify({
        "message": "Toy production key received successfully!",
        "toyProductionKey": toy_production_key
    }), 200


# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
