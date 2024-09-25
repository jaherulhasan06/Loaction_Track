# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Endpoint to receive location data
@app.route('/receive-location', methods=['POST'])
def receive_location():
    data = request.json
    lat = data['lat']
    lng = data['lng']
    
    # Print location to the console
    print(f"Received location: Latitude {lat}, Longitude {lng}")
    
    return jsonify({"status": "Location received", "lat": lat, "lng": lng})

if __name__ == '__main__':
    app.run(debug=True)
