# import cv2

# vid = cv2.VideoCapture("workout-rat.mp4")

# while True:
#     old,out = vid.read()
#     cv2.imshow("Workout Rat",out)
#     cv2.waitKey(1)
import cv2

vid = cv2.VideoCapture("IMG_4431.MOV")

while True:
    old,out = vid.read()
    out = cv2.resize(out, (500,800))
    out = cv2.putText(out,'2024 Recap',(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,255,0),2)
    # out = cv2.Canny(out,200,400)
    cv2.imshow("2024 Rewind",out)
    cv2.waitKey(6)
    