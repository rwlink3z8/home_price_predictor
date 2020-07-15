from flask import Flask, request, jsonify
from flask import render_template, flash, redirect
import json
import util

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('app.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    lot_size = float(request.form['lot_size'])
    bathrooms = int(request.form['bathrooms'])
    bedrooms = int(request.form['bedrooms'])
    yr_built = int(request.form['yr_built'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(total_sqft, lot_size, bedrooms, bathrooms, yr_built, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    from waitress import serve 
    serve(app, host="0.0.0.0", port=5000)
