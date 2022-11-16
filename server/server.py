from flask import Flask, request , jsonify
import util
import os
import base64
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/classify_image', methods=['GET','POST'])
def classify_image():
    image_data = request.files['image_data']
    image_string = base64.b64encode(image_data.read())
    response = jsonify(util.classify_image(image_string))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    print('Starting Flask Server')
    util.load_saved_artifacts()
    app.run(port=5000)