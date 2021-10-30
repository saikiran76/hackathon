from flask import Flask, render_template, request, url_for
import os
import pickle
import model as m
# from flaskalchemy.flaskalchemy import FlaskAlchemy
app=Flask(__name__,template_folder='templates')
model = pickle.load(open('expense.pkl','rb'))
@app.route("/" , methods = ['GET', 'POST'])# , methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        # if request.form['Prediction']:
        return render_template('survey.html')
    return render_template("index.html")

@app.route("/survey.html")
def formpage():
    return render_template("survey.html")

@app.route("/survey" , methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        name = request.form['name']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        
        q3 = float(q3)
        q4 = float(q4)
        q5 = float(q5)
        q2 = float(q2)
        q6 = float(q6)
        q7 = float(q7)
        # print(q2, q3, q4, q5, q6 , name)
        prediction = m.model(q2,q3,q4,q5,q6,q7)
        prediction = prediction - q7
        # print(type(prediction))
        if prediction > 30:
            return render_template("negative.html" , prediction = float(prediction))
        
            
    return render_template("survey.html")




if __name__ == "__main__":
    app.run(debug=True)