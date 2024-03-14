import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

def Compress_img(A, k):
    #Create SVD of the image matrix
    U, s, Vs = np.linalg.svd(A)
    #Start compressing
    Ar = np.zeros((len(U), len(Vs)))
    for i in range(k):
        #comput the low-rank approximation of U.T (transpose), s, V* and multiple the dot product(Matrix multiplication) together
        Ar += s[i] * np.outer(U.T[i], Vs[i])
    return Ar

#cmd: py Task_compress_image.py C:\Doc\EIE2112\sample_Lab2.jpg
inputimg = sys.argv[1] 
approximation = sys.argv[2]
outputimg = sys.argv[3]
#
approximation = int(approximation)
#input img as a matrix of the input jpg
img = np.asarray(mpimg.imread(inputimg))
print(repr(img))
img = Compress_img(img, approximation)
imgplot = plt.imshow(img)
plt.show()
plt.imsave(outputimg, img)