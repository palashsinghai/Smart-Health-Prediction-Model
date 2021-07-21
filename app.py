import numpy as np
import request
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pickle_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    int_features.extend([1,1])
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    if output == 0 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you have no disease')

    elif output == 1 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have tuberculosis') 

    elif output == 2 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have fever')

    elif output == 3 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have asthma')

    elif output == 4 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have pneumonia')

    elif output == 5 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have Chronic Bronchitis')

    elif output == 6 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have Hypothermia')

    elif output == 7 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have heart attack')

    elif output == 8 and request.method == 'POST':
        return render_template('disease.html', prediction_text='you may have stroke')
    else:
        return redirect(url_for('index'))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
