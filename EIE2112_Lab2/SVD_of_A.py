import numpy as np
# create a 5x6 matrix A with random integer values between 1 and 10
A = np.random.randint(1,10,size=(5, 6))
#print the values of the matrix
print("A=",A,'\n')
# and its shape
print("size(A)=",A.shape,'\n')
U, s, Vs = np.linalg.svd(A)
print("U=",U,'\n')
print("size(U)=",U.shape,'\n')
print("V*=",Vs,'\n')
print("size(V*)=",Vs.shape,'\n')