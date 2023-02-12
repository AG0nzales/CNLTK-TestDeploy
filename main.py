from turtle import title
from flask import Flask, redirect, request, render_template
import os
from joblib import load
from pos_tagger import predict_POS_model
from CNLTK import preprocessing, pos_tagger, ner
import string 

app = Flask(__name__)
# set file directory path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))    


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', title='Documentation')

@app.route("/api", methods=["GET", "POST"])
def api():
    return render_template('api.html', title='API Reference')

@app.route("/data", methods=["GET", "POST"])
def data():
    return render_template('data.html', title='CNLTK Data')

@app.route("/method", methods=["GET", "POST"])
def method():
    input = [request.form.get("pos")]
    print(input)
    converted_input = str(input[0])
    sentz, tagz = pos_tagger.predict_POS_model(converted_input)
    sentz2, tagz2 = ner.predict_NER_model(converted_input)
    
    # CLEANING 
    # sentz = " ".join(str(x) for x in sentz)
    # sentz = string.replace(",", "").replace("[", "").replace("]", "")
    
    # tagz = " ".join(str(x) for x in tagz)
    # tagz = string.replace("[", "").replace("]", "")
    
    # sentz2 = " ".join(str(x) for x in sentz2)
    # sentz2 = string.replace(",", "").replace("[", "").replace("]", "")
    
    # tagz2 = " ".join(str(x) for x in tagz2)
    # tagz2 = string.replace("[", "").replace("]", "")
    
    
    # PREPROCESSING
    # converted_input = " ".join(str(x) for x in converted_input)
    # converted_input = string.replace(",", "").replace("[", "").replace("]", "")
    preproc = preprocessing._POS(converted_input)
    
    
    return render_template('methods.html', title='CNLTK Methods', preproc = preproc[0], sentz = sentz, tagz=tagz, sentz2 = sentz2, tagz2 = tagz2)
    # return render_template('methods.html', title='CNLTK Methods')





if __name__ == '__main__':
#     app.run(debug=True)
      app.run(debug=False, host='0.0.0.0')
