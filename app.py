from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Current_Loan_Expenses =float(request.form['Current_Loan_Expenses'])
            Property_Age =float(request.form['Property_Age'])
            Loan_Amount_Request =float(request.form['Loan_Amount_Request'])
            Credit_Score =float(request.form['Credit_Score'])
            Property_Price =float(request.form['Property_Price'])
            Income_USD =float(request.form['Income_USD'])
       
         
            data = [Current_Loan_Expenses,Property_Age,Loan_Amount_Request,Credit_Score,Property_Price,Income_USD]
            data = np.array(data).reshape(1, 6)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(int(predict)))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)
     
#docker build -t loan-app .
#docker images
#docker run -p 8080:8080

#other terminal
#docker ps 
#docker stop dcd96d7d79b1
#docker images
#docker image rm -f loan-app
#docker build -t kumarkshitij152/loan-app .
#docker images
#docker push kumarkshitij152/loan-app:latest