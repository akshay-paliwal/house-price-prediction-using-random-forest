# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import os

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("main.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the use.
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            lstat = float(request.form['lstat'])

            filename = 'model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[rm, lstat, ptratio, nox, tax]])
            # showing the prediction results in a UI
            return render_template('predict.html', value=round(1000*prediction[0]))

        except:
            return ('Something Went Wrong')
    else:
        return render_template('main.html')


if __name__ == "__main__":
    app.run()