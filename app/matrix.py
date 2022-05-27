from functools import reduce
import math


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        
    # function to return matrix as a string
    def matrixToString(self):
        
        res = '\n'.join([','.join([str(x) for x in row]) for row in self.matrix])
        # print(res)
        return res
    
    # function to returns an inverted matrix
    def matrixInvert(self):
        res = list(map(list, zip(*self.matrix)))
        # convert to string same as matrixToString
        data = '\n'.join([','.join([str(x) for x in row]) for row in res])
        return data
    
    # function to return a flattened matrix
    def matrixFlatten(self):
        res = [x for row in self.matrix for x in row]
        # convert to a one line string
        data = ','.join([str(x) for x in res])
        
        return data
    
    # function to return sum of all integers in the matrix
    def matrixSum(self):
        # flatten with elements being integers
        res = [int(x) for row in self.matrix for x in row]
        # sum all integers in the matrix using reduce
        value = reduce(lambda x, y: x + y, res)
        return value
    
    # function to multiply all integers in the matrix
    def matrixProduct(self):
        # flatten with elements being integers
        res = [int(x) for row in self.matrix for x in row]
        # multiply all integers in the matrix using reduce
        value = reduce(lambda x, y: x * y, res)
        # print(value)
        return value