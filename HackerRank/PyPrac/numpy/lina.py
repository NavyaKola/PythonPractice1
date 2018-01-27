import numpy

A= [numpy.array(input().split(), float) for _ in range(int(input()))]
print (numpy.linalg.det(A))