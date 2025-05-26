import os
import pymongo

from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask-learn']


app = Flask(__name__)


@app.route('/signup',methods=['POST'])
def signup():
    try:
        form_data = dict(request.json)
        collection.insert_one(form_data) # it should be python dictionary
        return "Data added successfully!"
    except:
        print("Something went wrong!!")

@app.route('/view')
def view():
    try:
        data = collection.find()
        #to get data from the db
        data = list(data)
        # we need to make the data to a list format
        for item in data:
            print(item)
            del item['_id']
            #to hide a particular value from db
        return jsonify(data)
    except:
        print("Something went wrong")


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8081,debug=True)