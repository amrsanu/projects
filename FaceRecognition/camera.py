import cv2


def faceCapture():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while(True):
        ret, frame = cap.read()
        cv2.imshow('Input', frame)
        c = cv2.waitKey(1)
        # ASCII value of Esc is 27.
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    faceCapture()