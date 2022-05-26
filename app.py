import csv
from doctest import debug
from flask import Flask, request
from matrix import Matrix
# from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/echo', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
      f = request.files['file']
      # open file and read its contents
      data = []
      
      # read csv file
      with open(f.filename, 'r') as obj:
          # Return a reader object which will
          # iterate over lines in the given csvfile
          csv_reader = csv.reader(obj)
          
          # convert string to list
          data = list(csv_reader)
      # perform all matrix operations
      matrix = Matrix(data)
      
      # perform all matrix contents and join them as a string
      result = "*********** Matrix to String ***********\n" + matrix.matrixToString() + '\n' + "*********** Flatten Matrix ***********\n" + matrix.matrixFlatten() + '\n' + "*********** Inverted Matrix ***********\n" + matrix.matrixInvert() + '\n' + "*********** Product of all Elements ***********\n" + str(matrix.matrixProduct()) + '\n' + "*********** Sum of all Elements ***********\n" + str(matrix.matrixSum())
      
      return result
    return 'Hello, please upload a csv file!'

if __name__ == '__main__':
    app.run(debug=True)