import pickle
from sklearn import model_selection
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('G:\\projects\\flask API\\templates\\banglore_home_price_model.pickle', 'rb'))
np_array = np.zeros(16)
print(np_array)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age']
    glucose = request.form['avg_glucose_level']
    bmi = request.form['BMI']
    hyper = request.form['hypertension']
    heart = request.form['Heart_Disease']
    smoke = request.form['smoking_status_new']
    gender = request.form['Gender']
    married = request.form['ever_married']
    work = request.form['work_type']
    residence = request.form['Residence_type']

    np_array[0] = float(age)
    np_array[1] = float(glucose)
    np_array[2] = float(bmi)
    np_array[3] = float(hyper)
    np_array[4] = float(heart)
    np_array[5] = float(smoke)

    if gender == 1:
        np_array[6] = float(1)
    else:
        np_array[7] = float(1)

    if married == 'married':
        np_array[8] = float(1)
    else:
        np_array[9] = float(1)

    if work == 'Government':
        np_array[10] = float(1)
    elif work == 'Private':
        np_array[11] = float(1)
    elif work == 'Self-employed':
        np_array[12] = float(1)
    else:
        np_array[13] = float(1)

    if residence == 'Rural':
        np_array[14] = float(1)
    else:
        np_array[15] = float(1)

    model = pickle.load(open('G:\\projects\\flask API\\brain_stroke_prediction.pickle','rb'))

    prediction = model.predict([np_array])
    prediction = np.str(prediction)


    result = ""
    if prediction[0] == 1:
        result = ""



    return prediction



if __name__ == '__main__':
    app.run(debug=True)
