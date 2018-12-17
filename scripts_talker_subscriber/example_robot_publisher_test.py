import rospy
from std_msgs.msg import Float32
import numpy as np

if __name__ == '__main__':

    try:

        # name should not contain the space character
        rospy.init_node('controller_sphere_axis_target', anonymous=True)
        rate = rospy.Rate(10) # 10hz

        sphere_axis0_target = rospy.Publisher('/sphere_axis0/sphere_axis0/target', Float32, queue_size=10)
        sphere_axis1_target = rospy.Publisher('/sphere_axis1/sphere_axis1/target', Float32, queue_size=10)
        sphere_axis2_target = rospy.Publisher('/sphere_axis2/sphere_axis2/target', Float32, queue_size=10)

        sphere_axis0 = Float32()
        sphere_axis1 = Float32()
        sphere_axis2 = Float32()

        while not rospy.is_shutdown():

            sphere_axis0.data = -50
            sphere_axis1.data = 20
            sphere_axis2.data = -30

            sphere_axis0_target.publish(sphere_axis0)
            sphere_axis1_target.publish(sphere_axis1)
            sphere_axis2_target.publish(sphere_axis2)

            rate.sleep()

    except rospy.ROSInterruptException:
        pass