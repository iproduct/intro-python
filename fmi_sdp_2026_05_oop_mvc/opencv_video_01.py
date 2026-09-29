import cv2 as cv

if __name__ == '__main__':
    print(f'Opencv version: {cv.version.opencv_version}')
    video = cv.VideoCapture(0)
    while True:
        success, img = video.read()
        cv.imshow('Video', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break;
    video.release()
    cv.destroyAllWindows()