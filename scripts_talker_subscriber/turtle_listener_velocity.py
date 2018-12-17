import rospy
from geometry_msgs.msg import Twist

def callback(data):
    print("twist.linear.x = %s", data.linear.x)
    print("\n")
    print("twist.angular.z = %s", data.angular.z)

def listener():

    # In ROS, nodes are uaniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('turtle_listener_velocity', anonymous=True)

    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
