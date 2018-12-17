import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty
import numpy as np

class class_pose_message:

    def __init__(self):
        # initialise variables

        self.x_last = None
        self.y_last = None
        self.yaw_last = None
        self.time_last = None

        self.x_current = None
        self.y_current = None
        self.yaw_current = None

        self.distance = 0

        self.first_loop = True
        
    def update(self):
        self.x_last = self.x_current
        self.y_last = self.y_current
        self.yaw_last = self.yaw_current

        self.time_last = self.time_current

    def calculate_velocity(self):
        diff_x = self.x_current - self.x_last
        diff_y = self.y_current - self.y_last
        diff_time = time.time() - self.time_last

        self.velocity_x = diff_x/diff_time
        #print(self.velocity_x)

    def calculate_distance(self):
        diff_x = np.power(self.x_current - self.x_last, 2)
        diff_y = np.power(self.y_current - self.y_last, 2)
        new_distance = np.sqrt(diff_x + diff_y)

        self.distance =  self.distance + new_distance
        print(self.distance)

    def Callback_pose(self, pose_message):
        self.time_current = time.time()
        self.x_current = pose_message.x
        self.y_current = pose_message.y
        self.yaw_current = pose_message.theta

        if(self.first_loop):
            self.first_loop = False
            self.update()

        else:
            self.calculate_velocity()
            self.calculate_distance()
            self.update()


if __name__ == '__main__':

    rospy.init_node('turtle_listener_pose', anonymous=True)
    
    cnum = class_pose_message()
    rospy.Subscriber('/turtle1/pose', Pose, cnum.Callback_pose)

    rospy.spin()