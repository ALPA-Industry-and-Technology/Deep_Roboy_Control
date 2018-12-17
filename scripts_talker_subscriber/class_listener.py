import rospy
from turtlesim.msg import Pose

class class_callback:

    def __init__(self):
        # initialise variables
        self.a = None

    def callback(self, data):
        self.a = data.x

if __name__ == '__main__':

    rospy.init_node('turtle_listener_pose', anonymous=True)
    
    cnum = class_callback()

    #sub_one = None
    #sub_one = rospy.Subscriber('/turtle1/pose', Pose, cnum.callback, sub_one)

    rospy.Subscriber('/turtle1/pose', Pose, cnum.callback)

    print(cnum.a)

    rospy.spin()
