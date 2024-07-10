import numpy as np
def calculate(n,matrix,mat):
    l1 = [list(matrix.mean(axis = 0)),list(matrix.mean(axis=1)),mat.mean()]
    l2 = [list(matrix.var(axis = 0)),list(matrix.var(axis=1)),mat.var()]
    l3 = [list(matrix.std(axis = 0)),list(matrix.std(axis=1)),mat.std()]
    l4 = [list(matrix.max(axis = 0)),list(matrix.max(axis=1)),mat.max()]
    l5 = [list(matrix.min(axis = 0)),list(matrix.min(axis=1)),mat.min()]
    l6 = [list(matrix.sum(axis = 0)),list(matrix.sum(axis=1)),mat.sum()]
    result = {'mean': l1,
              'variance': l2,
              'standard deviation': l3,
              'max': l4,
              'min': l5,
              'sum': l6}
    return result
n = list(map(int,input().split()))
try:
    mat = np.array(n)
    matrix = np.array(n).reshape(3,3)
    print(calculate(n,matrix,mat))
except ValueError as e:
    print("List must contain nine numbers")
