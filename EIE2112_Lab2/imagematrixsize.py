import numpy as np
import matplotlib.pyplot as plt
import sys

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

#cmd: py  C:\Doc\EIE2112\sample_Lab2.jpg C:\Users\wwwnh\EIE2112_Lab2_kvalue\kvalue100.jpg
inputimg =  'C:\Doc\EIE2112\sample_Lab2.jpg'
approximation = 10

#
approximation = int(approximation)
#read img as a matrix of the input jpg
image = plt.imread(inputimg)
#input jpg image into the function 
print(image.shape)
print(len(image))
print(len(image[0]))
image = Compress_img(image, approximation)
print(image.shape)
plt.imshow(image, cmap = 'gray')
plt.show()
