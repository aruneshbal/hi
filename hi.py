import cv2
def hi():
    Videotaken=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=Videotaken.read()
        cv2.imwrite("hello.jpg",frame) 
    Videotaken.release()
    cv2.destroyAllWindows()
hi()
       