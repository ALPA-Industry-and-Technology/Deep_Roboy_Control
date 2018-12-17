import rospy
# Type is geometry_msgs/Twist
from geometry_msgs.msg import Twist
import numpy as np


def move():
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # name should not contain the space character
    rospy.init_node('talker_turtle_velocity', anonymous=True)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        twist = Twist()

        twist.linear.x = -0.1
        
        # no effect:
        #twist.linear.y = -2.0
        #twist.linear.z = -4.0
        #twist.angular.x = 1.0
        #twist.angular.y = 1.0

        twist.angular.z = 0.0

        # print twist
        #rospy.loginfo(twist)

        speed_publisher.publish(twist)
        rate.sleep()

if __name__ == '__main__':

    try:
        move()
    except rospy.ROSInterruptException:
        pass

