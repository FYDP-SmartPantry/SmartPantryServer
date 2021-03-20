from flask import Flask, flash, request, redirect, url_for, jsonify
import os
from werkzeug.utils import secure_filename
import json
from flask import send_from_directory
from food_prediction import food_dect
from PIL import Image
from pymongo import MongoClient
from datetime import datetime
from bson import json_util
import pymongo

app = Flask(__name__)
UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['jpg','png','jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/predict', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            image_url = url_for('uploaded_file', filename=filename)
            re = food_dect(os.path.join(app.config['UPLOAD_FOLDER'], filename),"resnet50_weights_tf_dim_ordering_tf_kernels.h5")
            
            return {"result": {"prediction": re}}#,"probability": po}}
            #return '''<h1>The prediction is: {} {}</h1><img src="{}" height = "85" width="200"/>'''.format(re,po, image_url)


    return '''
    <!doctype html>
    <title>Upload new Photo</title>
    <h1>Upload a jpg/png/jpeg of vegetable or fruit</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/store', methods=['POST'])
def store():
    data = json.loads(request.data)
    record = {"user_id": data['user_id'],
              "food_inventory": data['food_inventory'],
              "waste_inventory": data['waste_inventory'],
              "timestamp": datetime.now()}
    with MongoClient() as client:
        db = client.inventory
        col =  db.inventory
        col.insert_one(record)
    return "Inventory information stored!"


@app.route('/retrieve', methods=['POST'])
def retrieve():
    data = json.loads(request.data)
    user_id = data['user_id']
    with MongoClient() as client:
        db = client.inventory
        col =  db.inventory
        user_cursor = col.find({"user_id": user_id}).sort('timestamp',pymongo.DESCENDING)
    user_cursor = json.loads(json_util.dumps(user_cursor))
    result = {"records":[]}
    for record in user_cursor:
        record['timestamp']['$date'] = datetime.fromtimestamp(int(record['timestamp']['$date'])/1000).strftime('%Y-%m-%d %H:%M:%S')
        result['records'].append(record)
    return result




if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)
