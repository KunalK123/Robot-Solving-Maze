from robot_control_class import RobotControl
import time as t
rc = RobotControl()
rc.stop_robot()
while True:
    d = rc.get_laser(360)
    f = rc.get_laser(0)
    
    if(d < 1.0):
        #Stop Robot
        rc.stop_robot()
        rc.turn("clockwise", 0.3, 5.25)
        if (d < 1.0 and f < 1.3):
            rc.stop_robot()
            rc.turn("counterclockwise", 0.6, 5.35)
    else:
        #Move Forward
        rc.move_straight()

    print("distance1 = ", d)
    print("distance2 = ", f)
