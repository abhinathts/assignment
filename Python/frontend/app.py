import requests

from flask import Flask, request,render_template
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8081"

app = Flask(__name__)
@app.route('/')
def hello():
    try:
        today = datetime.today().strftime('%A')
        current_time = datetime.now().strftime('%H:%M:%S')
        return render_template('index.html', day_is=today, current_time=current_time)
    except:
        print("Something went wrong") 

@app.route('/signup',methods=['POST'])


def signup():
    try:
        form_data = dict(request.form)
        requests.post(BACKEND_URL + '/signup', json=form_data)

        return "Data added successfully!"
    except:
        print("Something went wrong")    

@app.route('/get_data')
def get_data():
    try:
        response = requests.get(BACKEND_URL+'/view')

        return response.json()
    except:
        print("Something went wrong") 


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)


from flask  import Flask
app = Flask(__name__)
@app.route('/api')
def api():
    files = open('data.json','r')
    data = files.read()
    return (data)
if __name__ == '__main__':
    app.run(debug=True)
