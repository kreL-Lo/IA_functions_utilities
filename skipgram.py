import numpy as np
import math 
#row : reprezinta pozitia cuvantului in matrice
# se baga nr de aparitii
words =['beef','cabage','parsley']
matrix_doc =[
    [1,0,0],
    [0,1,2],
    [1,6,1]
]

matrix = np.array(matrix_doc)

d = matrix[0]+matrix[1]

def cosine(table,row1,row2):
    sum1 = sum(table[row1]*table[row2])
    prod_sqr_A =math.sqrt(sum(i *i for i in table[row1]))
    prod_sqr_B = math.sqrt(sum(i *i for i in table[row2]))
    return sum1/(prod_sqr_A*prod_sqr_B)

print('Similaritati folosind COSINE FUNCTION')
for i in range(0,3):
    for j in range(i,3):
        if i!=j:
            print(words[i],words[j],':',cosine(matrix,i,j))


