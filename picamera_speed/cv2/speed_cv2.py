import time
import cv2

def test_resolution(width, height):
    time_start = time.perf_counter()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    _, frame = cap.read()
    cv2.imwrite("capture({}, {}).jpg".format(width, height), frame)
    time_stop = time.perf_counter()
    with open('tests.txt', 'a') as f:
        data = "\n{}x{} - {}".format(width, height, time_stop - time_start)
        print(data)
        f.write(data)        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":  
    # picamera V2 version  
    #width = [640, 1280, 1640, 1640, 1920, 3280]
    #height =[480,  720,  922, 1232, 1080, 2464]
    
    # picamera V1 version 
    width = [640, 1296, 1296,  1920, 2592]
    height =[480,  730, 972, 1080, 1944]

    for test_width, test_height in zip(width, height):
        test_resolution(test_width, test_height)