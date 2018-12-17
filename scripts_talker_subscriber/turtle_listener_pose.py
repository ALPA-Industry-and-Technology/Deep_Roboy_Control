import rospy
from turtlesim.msg import Pose

def callback(data):
    print("Pose.x = " + str(data.x))

def listener():

    rospy.init_node('turtle_listener_pose', anonymous=True)

    rospy.Subscriber('/turtle1/pose', Pose, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
