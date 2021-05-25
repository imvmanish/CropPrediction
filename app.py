from flask import Flask, render_template ,request
from flask import jsonify, make_response
import joblib
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

def weather_api(city_name):
    API_key = '2eb7f9289b3e6ee8b9d43ec77776e0fa'
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
    return response.json()

def kelvin_to_celsius(kelvin):
    celsius = float(kelvin) - 273.15
    return celsius

def crop_name(crop_number):
    dict = {
    1: 'Ground Nut',
    2: 'Chickpea',
    3: 'Peas',
    4: 'watermelon',
    5: 'apple',
    6: 'banana',
    7: 'papaya',
    8: 'millet',
    9: 'Lentil',
    10: 'Adzuki Beans',
    11: 'rice',
    12: 'maize',
    13: 'wheat',
    14: 'Mung Bean',
    15: 'Moth Beans',
    16: 'Black gram',
    17: 'Jute',
    18: 'Sugarcane',
    19: 'orange',
    20: 'Rubber',
    21: 'Kidney Beans',
    22: 'pomegranate',
    23: 'grapes',
    24: 'Tobacco',
    25: 'Pigeon Peas',
    26: 'Tea',
    27: 'Coffee',
    28: 'Cotton',
    29: 'muskmelon',
    30: 'mango',
    31: 'Coconut'
    }
    answer = dict[crop_number]
    return answer

@app.route('/prediction',methods=["POST"])
def predict_crop():
    model = joblib.load('crop-predictor.joblib')
    place = request.form['place']
    rainfall = request.form['rainfall']
    ph = request.form['ph']
    output = weather_api(place)
    temperature = output['main']['temp']
    humidity = float(output['main']['humidity'])
    temp = kelvin_to_celsius(temperature)
    prediction = model.predict([[temp,humidity,ph,rainfall]])
    prediction = int(prediction)
    crop_name_predicted = crop_name(prediction)
    return crop_name_predicted

if __name__ == "__main__":
    app.run(debug=True,port=8000)