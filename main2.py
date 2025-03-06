from djitellopy import Tello
import time
drone1=Tello()
drone1.connect()
print(drone1.get_battery())
drone1.takeoff()
time.sleep(1)
x=0
y=0
while True:
    drone1.send_rc_control(int(x),int(x),0,int(y))
    time.sleep(0.5)
    x+=3
    y+=7
    if y>80:
        break
drone1.send_rc_control(0,0,0,0)
drone1.land()