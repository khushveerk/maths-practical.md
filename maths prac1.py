## practical 1 :Find Cofactors , Determinant, Adjoint and Inverse of a matrix . 
#using numpy
# taking input of matrix from user ( user define matrix input )

import numpy as np
NR =int(input("Enter the number of rows:"))
NC =int(input("Enter the number of columns:"))

print("Enter the entries in asingle line (separated by space) :")

entries =list(map(int ,input().split()))
A =np.array(entries).reshape(NR,NC)
print("Matrix A is as follows :",'\n',A)


A_inverse =np.linalg.inv(A)

Transpose_of_A_inverse =np.transpose(A_inverse)

Determinant_of_A =np.linalg.det(A)

Cofactor_of_A =np.dot(Transpose_of_A_inverse,Determinant_of_A )

print("The Cofactor of a matrix is:",'\n',Cofactor_of_A)

print("The Determinant of a matrix is:",'\n',Determinant_of_A)

Adjoint_of_A =np.transpose(Cofactor_of_A)
print("The Adjoint of a matrix is:",'\n',Adjoint_of_A)

