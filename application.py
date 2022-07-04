from flask import Flask
from flask import request
import inferencer as inf
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/inference', methods=['POST'])
def inference_uploaded_file():
    f = request.files['img']

    return {"result": inf.run_inference(f)}

if __name__ == '__main__':
    app.run(debug=True)