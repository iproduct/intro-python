import numpy as np
import cv2 as cv
from book import Book


if __name__ == '__main__':
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr)
    print("OpenCV version:", cv.version.opencv_version)
    mybook = Book(1,"saddsad","sdfdsfds",["sdfsd"],["sdfsd"],"1999","English")
    print(mybook._internal)
    print("get_iternal():", mybook.get_internal())
