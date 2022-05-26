from flask import Flask, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
    if request.method == 'POST':
      f = request.files['file']
    #   f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
    return 'Hello, please upload a csv file!'

if __name__ == '__main__':
    app.run()