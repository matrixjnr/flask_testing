# read contents of csv file matrix.csv and write unittests for the Matrix class
# using pytest
import pytest
import csv

from app.matrix import Matrix

# read matrix.csv
data = []
with open('matrix.csv', 'r') as obj:
    # Return a reader object which will
    # iterate over lines in the given csvfile
    csv_reader = csv.reader(obj)
  
    # convert string to list
    data = list(csv_reader)
    
# test Matrix methods
def testMatrix1():
    matrix = Matrix(data)
    # Test matrixToString
    assert matrix.matrixToString() == '1,2,3\n4,5,6\n7,8,9'

# test Matrix methods
def testMatrix2():
    matrix = Matrix(data)
    # Test matrixFlatten
    assert matrix.matrixFlatten() == '1,2,3,4,5,6,7,8,9'

# test Matrix methods
def testMatrix3():
    matrix = Matrix(data)
    # Test matrixInvert
    assert matrix.matrixInvert() == '1,4,7\n2,5,8\n3,6,9'

# test Matrix methods
def testMatrix4():
    matrix = Matrix(data)
    # Test MatrixProduct
    assert matrix.matrixProduct() == 362880

# test Matrix methods
def testMatrix5():
    matrix = Matrix(data)
    # Test MatrixSum
    assert matrix.matrixSum() == 45
    