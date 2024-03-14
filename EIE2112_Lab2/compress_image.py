import numpy as np
import matplotlib.pyplot as plt
import sys

def downsampling(A, filter_size):
    dim = A.shape[0]

#function for compression, low-rank approximation for the image matrix
def Compress_img(A, k):
    #Create SVD of the image matrix
    U, s, Vs = np.linalg.svd(A)
    #Start compressing
    #Create a matrix (Ar) of content 0 with the size of U and V*
    Ar = np.zeros((len(U), len(Vs)))
    #for i from 0 to k (approximatino), 
    #input the dot product between U, s, V* into Ar 
    for i in range(k):
        #compute the low-rank approximation of 
        #U.T (transpose), s, V* and multiple the dot product(Matrix multiplication) together
        Ar += s[i] * np.outer(U.T[i], Vs[i])
    return Ar

inputimg = sys.argv[1] 
approximation = sys.argv[2]
outputimg = sys.argv[3]
#
approximation = int(approximation)
#read img as a matrix of the input jpg
image = plt.imread(inputimg)
#input jpg image into the function 
image = Compress_img(image, approximation)
#save the matrix as a jpg
plt.imsave(outputimg, image, cmap = 'gray')