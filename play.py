import csv

from matrix import Matrix

# read matrix.csv
data = []
with open('matrix.csv', 'r') as obj:
    # Return a reader object which will
    # iterate over lines in the given csvfile
    csv_reader = csv.reader(obj)
  
    # convert string to list
    data = list(csv_reader)
    
matrix = Matrix(data)

print(matrix.matrixToString())
print(matrix.matrixFlatten())
print(matrix.matrixInvert())
print(matrix.matrixProduct())
print(matrix.matrixSum())