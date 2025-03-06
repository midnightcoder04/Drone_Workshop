import keyboard
import cv2

print("Press 'WASD' or Arrow keys. Press 'ESC' to exit.")

while True:
    if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
        print("Moving Up")
        cv2.waitKey(100)
    elif keyboard.is_pressed("s"):
        print("Moving Down")
        cv2.waitKey(100)
    elif keyboard.is_pressed("down"):
        print("Moving Down with arrow ")
        cv2.waitKey(100)
    

        
    elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
        print("Moving Left")
        cv2.waitKey(100)

    elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
        print("Moving Right")
        cv2.waitKey(100)
    elif keyboard.is_pressed("esc"):
        print("Exiting...")
        break
