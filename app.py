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

# def kelvin_to_celcius():

@app.route('/prediction',methods=["POST"])
def predict_crop():
    model = joblib.load('crop-predictor.joblib')
    place = request.form['place']
    rainfall = request.form['rainfall']
    ph = request.form['ph']
    output = weather_api(place)
    temperature = output['main']['temp']
    humidity = output['main']['humidity']
    return output 
    # prediction = model.predict([[20,82,6.57,92]])
    # return str(prediction)

if __name__ == "__main__":
    app.run(debug=True,port=8000)