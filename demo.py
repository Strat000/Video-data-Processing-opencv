import cv2
import time

if __name__ == '__main__':
    cap = cv2.VideoCapture('video.mp4')

    if not cap.isOpened():
        print('Error opening video stream or file')
        exit(0)
    
    print('Video properties:')
    print('Video Dimension: ', cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('Video FPS: ', cap.get(cv2.CAP_PROP_FPS))

    while(cap.isOpened()):
        ret, img = cap.read()
        if ret:
            imgin = img[:, :, (2,1,0)] # BGR to RGB (OpenCV uses BGR)
        else:
            break

        cv2.imshow('camOut', img)
        cv2.waitKey(1)

    cap.release()