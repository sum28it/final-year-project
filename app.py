# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load the Random Forest CLassifier model
filename = 'ml_model'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        BMI = int(request.form['bmi'])
        Smoking = int(request.form['smoking'])
        AlcoholDrinking = int(request.form['alcoholDrinking'])
        Stroke = request.form.get('stroke')
        PhysicalHealth = int(request.form['physicalHealth'])
        MentalHealth = float(request.form['mentalHealth'])
        DiffWalking = request.form.get('diffWalk')
        Sex = request.form.get('sex')
        AgeCategory = request.form.get('ageCat')
        Race = request.form.get('race')
        Diabetic = request.form.get('diabetic')
        PhysicalActivity = request.form.get('physicalActiv')
        GenHealth = request.form.get('genHealth')
        SleepTime = request.form.get('sleeptime')
        Asthma = request.form.get('asthma')
        KidneyDisease = request.form.get('kidneyDisease')
        SkinCancer = request.form.get('skinCancer')
        
        data = np.array([[BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5000)


