'''两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：'''

import numpy

x = numpy.array([[12,7,3],
                 [4 ,5,6],
                 [7 ,8,9]])
y = numpy.array([[5,8,1],
                 [6,7,3],
                 [4,5,9]])
z=x+y
print(z)