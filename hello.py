import cv2
def take_pic():
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        cv2.imwrite("new pic.jpg",frame)
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
take_pic()