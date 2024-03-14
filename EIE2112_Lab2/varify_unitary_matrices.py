import numpy as np
# create a 5x6 matrix A with random integer values between 1 and 10
A = np.random.randint(1,10,size=(5, 6))
#print the values of the matrix
print("A=",A,'\n')
# and its shape
print("size(A)=",A.shape,'\n')
U, s, Vs = np.linalg.svd(A)
# https://numpy.org/doc/stable/reference/generated/numpy.zero.html
S = np.zeros(A.shape)
# https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html
np.fill_diagonal(S,s,wrap=True)
# Note: np.matmul computes the product between two matrices
# see http://numpy.org/doc/stable/reference/generated/numpy.matmul.html
Ar = np.matmul(np.matmul(U, S), Vs)
print("U*inv(U)=",np.matmul(U,np.linalg.inv(U)),'\n')
print("Vs*inv(Vs)=",np.matmul(Vs,np.linalg.inv(Vs)))