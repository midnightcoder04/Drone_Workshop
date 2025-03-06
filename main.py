import cv2
from djitellopy import Tello
import keyboard

drone = Tello()
drone.connect()
print(drone.get_battery())


# Launch
drone.takeoff()
cv2.waitKey(1000)

# Start
import keyboard
import cv2


while True:
    if keyboard.is_pressed("w"):
        drone.move_forward(30)
        cv2.waitKey(100)
    elif keyboard.is_pressed("s"):
        drone.move_back(30)
        cv2.waitKey(100)
    elif keyboard.is_pressed("a"):
        drone.move_left(30)
        cv2.waitKey(100)
    elif keyboard.is_pressed("d"):
        drone.move_right(30)
        cv2.waitKey(100)
    elif keyboard.is_pressed("up"):
        drone.move_up(30)
        cv2.waitKey(100)
    elif keyboard.is_pressed("down"):
        drone.move_down(30)
        cv2.waitKey(100)
    elif keyboard.is_pressed("left"):
        drone.rotate_counter_clockwise(45)
        cv2.waitKey(100)
    elif keyboard.is_pressed("right"):
        drone.rotate_clockwise(45)
        cv2.waitKey(100)
    elif keyboard.is_pressed("esc"):
        print("Exiting...")
        break