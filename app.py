import os
import pickle
from flask import Flask, request, jsonify, render_template
from utils import get_route_suggestion, get_alert

app = Flask(__name__)

# Load the trained ML model
MODEL_FILE = 'model.pkl'

# Initialize model variable
model = None

# Load the model at startup if it exists
if os.path.exists(MODEL_FILE):
    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)
else:
    print(f"Warning: {MODEL_FILE} not found. Please train the model before making predictions.")

@app.route('/', methods=['GET'])
def index():
    """Serves the test UI frontend."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predicts delivery delay using the loaded ML model.
    Expects input JSON format:
    {
      "distance": number,
      "traffic": 1 | 2 | 3,
      "weather": 0 | 1
    }
    """
    if model is None:
        return jsonify({"error": "Model not trained yet."}), 500

    try:
        data = request.get_json()
        
        # Extract features
        distance = float(data.get('distance', 0))
        traffic = int(data.get('traffic', 1))
        weather = int(data.get('weather', 0))
        priority = int(data.get('priority', 1))
        vehicle = int(data.get('vehicle', 2))
        try:
            expected_time = float(data.get('time', 0))
        except ValueError:
            expected_time = 0.0
        route_name = data.get('routeName', 'Unknown Route')
        
        # Make delay prediction. model.predict expects a 2D array.
        prediction_result = model.predict([[distance, traffic, weather]])
        delay_prediction = int(prediction_result[0])
        
        # Calculate confidence probability of a delay (class 1)
        # predict_proba returns [[prob_class_0, prob_class_1]]
        prob = model.predict_proba([[distance, traffic, weather]])[0][1]
        confidence = round(prob * 100, 2)
        
        # Determine route optimization and alerts via helper functions
        route_suggestion = get_route_suggestion(distance, traffic, weather, priority, vehicle, expected_time, route_name)
        alert_msg = get_alert(weather, traffic, priority, delay_prediction)
        
        # Final JSON payload structure
        response = {
            "delay_prediction": delay_prediction,
            "route_suggestion": route_suggestion,
            "alert": alert_msg,
            "confidence": confidence
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run server locally; for Render, this will be handled by Gunicorn
    app.run(host='0.0.0.0', port=5000, debug=True)
