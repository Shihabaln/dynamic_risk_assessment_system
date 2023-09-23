from flask import Flask, session, jsonify, request
import pandas as pd
import json
import os
import subprocess
import diagnostics as dg

with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 

######################Set up variables for use in our script
app = Flask(__name__)

@app.route('/')
def index():
    print("Starting index...")
    return "Welcome to our application! Here, you can forecast whether an employee has departed from the company."


@app.route("/prediction", methods=['POST','OPTIONS'])
def predict():        
    """
    call the prediction function you created in Step 3
    
    Returns:
        preds_json: model predictions
    """
    filepath = request.get_json()['filepath']

    data = pd.read_csv(filepath)
    features = ["lastmonth_activity", "lastyear_activity", "number_of_employees"]
    X = data[features]
    

    preds = dg.model_predictions(X)
    preds_json = jsonify(preds.tolist())
    
    return preds_json


@app.route("/scoring", methods=['GET','OPTIONS'])
def calculate_score():        
    """
    Scoring endpoint that runs the script scoring.py and
    gets the score of the deployed model
    
    Returns:
        str: model f1 score
    """
    
    result = subprocess.run(['python', 'scoring.py'],capture_output=True)
    # Get the output of the function as a string
    output_str = result.stdout.decode('utf-8')

    return output_str


#Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def stats():        
    """
    Calls summary statistics functions from diagnostics module
    """
    return jsonify(dg.dataframe_summary())


#Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnostics():        
    
    #Get functions results
    missing = dg.get_missings()
    time = dg.execution_time()
    outdated = dg.outdated_packages_list()

    results = {
        'missing_percentage': missing,
        'execution_time': time,
        'outdated_packages': outdated
    }

    return jsonify(results)


#Prediction Endpoint
if __name__ == "__main__":
    print("Starting app")
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)