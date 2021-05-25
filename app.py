from flask import Flask, render_template ,request
import joblib
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

def weather_api():
    

@app.route('/prediction',methods=["POST"])
def predict_crop():
    model = joblib.load('crop-predictor.joblib')
    place = request.form['place']
    rainfall = request.form['rainfall']
    ph = request.form['ph']
    prediction = model.predict([[20,82,6.57,92]])
    return str(prediction)

if __name__ == "__main__":
    app.run(debug=True,port=8000)