import cv2,os,serial,sys,time

raghu=cv2.VideoCapture(0) 
raghu.set(3,320)
raghu.set(4,240) #setting width and height pixels
#os.mkdir("/Users/RAGHUNADH/Desktop/intrusion")
#print(os.listdir()) returns list of files in directory
#print(os.curdir) returns a . in windows and linux and : in mac
#print(os.getcwd()) returns a current working directory
i=0
decoding=serial.Serial('COM3',115200)

    
    
while True:
    output=decoding.read_all().decode().split("\r\n")
    if len(output)==1:
        feed=0
        pass
    else:
        feed=int(output[-2])
        print(feed)
        
    if feed>5 and feed<20:                      

        ret,frame=raghu.read()
        path="/Users/RAGHUNADH/Desktop/intrusion/"+"frame"+str(i)+".jpg"
        cv2.imshow("raghu",frame)
        cv2.imwrite(path,frame)
        i+=1
    time.sleep(0.5)
#cv2.waitKey(0)     closes when there is a keypress event
    cv2.destroyAllWindows()

