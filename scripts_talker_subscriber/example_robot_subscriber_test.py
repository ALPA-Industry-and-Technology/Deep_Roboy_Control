import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from roboy_communication_simulation.msg import JointState, Tendon
import numpy as np

class receiving_data:

    # def __init__(self):
    #     self.sphere_axis0_target = None
    #     self.sphere_axis1_target = None
    #     self.sphere_axis2_target = None

    def sphere_axis0_callback(self, data):
        # data: 1.00530970097

        self.sphere_axis0_target = data.data
        #print("sphere_axis0 = " + str(data.data))

    def sphere_axis1_callback(self, data):
        # data: 1.00530970097 

        self.sphere_axis1_target = data.data
        #print("sphere_axis1 = " + str(data.data))

    def sphere_axis2_callback(self, data):
        # data: 1.00530970097

        self.sphere_axis2_target = data.data
        #print("sphere_axis2 = " + str(data.data))

class sending_data:

    # def __init__(self):
    #     self.robot_state_position_x = None
    #     self.robot_state_target_position_x = None

    #     self.joint_state_origin = None
    #     self.joint_state_axis_x = None

    def robot_state_callback(self, data):

        # header: 
        #   seq: 1173271
        #   stamp: 
        #     secs: 1541776096
        #     nsecs: 726518639
        #   frame_id: "top"
        # pose: 
        #   position: 
        #     x: -0.000876786354214
        #     y: -0.0383262762159
        #     z: 0.255639769326
        #   orientation: 
        #     x: 0.368067755957
        #     y: 3.61353925429e-05
        #     z: -8.91476544988e-06
        #     w: 0.929798970552

        self.robot_state_position_x = data.pose.position.x
        #print(self.robot_state_position_x)

        self.robot_state_orientation_x = data.pose.orientation.x
        #print( "robot_state_orientation_x: " + str(self.robot_state_orientation_x) )

    def robot_state_target_callback(self, data):

        # header: 
        #   seq: 89379
        #   stamp: 
        #     secs: 1541829536
        #     nsecs: 242169076
        #   frame_id: "top"
        # pose: 
        #   position: 
        #     x: 0.0470758314421
        #     y: -0.0174977001292
        #     z: 0.233450130438
        #   orientation: 
        #     x: -0.132498556232
        #     y: 0.572061380279
        #     z: -0.415626957605
        #     w: 0.69458199077

        self.robot_state_target_position_x = data.pose.position.x
        #print(self.robot_state_target_position_x)

        self.robot_state_target_orientation_x = data.pose.orientation.x
        #print( "robot_state_target_orientation_x: " + str(self.robot_state_target_orientation_x) )

    def joint_state_callback(self, data):

        # names: [sphere_axis0, sphere_axis1, sphere_axis2]
        # origin: 
        # - 
        #     x: -0.00088
        #     y: -0.00205
        #     z: 0.217
        # - 
        #     x: -0.00088
        #     y: -0.00205
        #     z: 0.217
        # - 
        #     x: -0.00088
        #     y: -0.00205
        #     z: 0.217
        # axis: 
        # - 
        #     x: 1.0
        #     y: 0.0
        #     z: 0.0
        # - 
        #     x: 0.0
        #     y: 0.770513253313
        #     z: 0.637423977012
        # - 
        #     x: 0.844327953266
        #     y: -0.341548818758
        #     z: 0.412861613302
        # torque: [0.0, 0.0, 0.0]

        self.joint_state_name = data.names
        #print(self.joint_state_name)

        #self.joint_state_origin = data.origin[0].x
        self.joint_state_origin = data.origin
        #print(self.joint_state_origin)

        self.joint_state_axis = data.axis
        #print(self.joint_state_axis) 

    def joint_state_target_callback(self, data):

        # names: [sphere_axis0, sphere_axis1, sphere_axis2]
        # origin: 
        # - 
        #     x: -0.00088
        #     y: -0.00205
        #     z: 0.217
        # - 
        #     x: -0.00088
        #     y: -0.00205
        #     z: 0.217
        # - 
        #     x: -0.00088
        #     y: -0.00205
        #     z: 0.217
        # axis: 
        # - 
        #     x: 1.0
        #     y: 0.0
        #     z: 0.0
        # - 
        #     x: 0.0
        #     y: 0.770513253313
        #     z: 0.637423977012
        # - 
        #     x: 0.844327953266
        #     y: -0.341548818758
        #     z: 0.412861613302
        # torque: [0.0, 0.0, 0.0]

        self.joint_state_target_name = data.names
        #print(self.joint_state_name)

        #self.joint_state_origin = data.origin[0].x
        self.joint_state_target_origin = data.origin
        #print(self.joint_state_origin)

        self.joint_state_target_axis = data.axis
        #print(self.joint_state_axis) 

    def tendon_state_callback(self, data):

        # name: [motor0, motor1, motor2, motor3, motor4, motor5, motor6, motor7]
        # force: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # l: [0.6698735356330872, 0.42564302682876587, -0.2495754063129425, -0.013258818536996841, -0.5348357558250427, -0.0356149859726429, 0.5202829837799072, 0.41714781522750854]
        # ld: [-2.364873921689714e-11, 1.1245370086510054e-11, -6.957939779894673e-11, -4.756403951255983e-11, 5.416414192160879e-11, 2.467460957777945e-11, 9.67225674552985e-11, 6.824774079206009e-11]
        # number_of_viapoints: [4, 3, 4, 3, 4, 3, 4, 3]
        # viaPoints: 
        # - 
        #     x: -0.0465999990702
        #     y: -0.041657872498
        #     z: 0.0845757871866
        # -  this 8 times

        # is constantly zero
        self.tendon_state_force = data.force
        #print(self.tendon_state_force)

        self.tendon_state_l = data.l
        #print(self.tendon_state_l)

        self.tendon_state_ld = data.ld
        #print(self.tendon_state_ld)



if __name__ == '__main__':

    try:
        rospy.init_node('subscriber_cardsflow_example_CARDSFlow', anonymous=True)

        CARDSFlow_receiving_data = receiving_data()
        rospy.Subscriber('/sphere_axis0/sphere_axis0/target', Float32, CARDSFlow_receiving_data.sphere_axis0_callback)
        rospy.Subscriber('/sphere_axis1/sphere_axis1/target', Float32, CARDSFlow_receiving_data.sphere_axis1_callback)
        rospy.Subscriber('/sphere_axis2/sphere_axis2/target', Float32, CARDSFlow_receiving_data.sphere_axis2_callback)

        CARDSFlow_sending_data = sending_data()
        rospy.Subscriber('/robot_state', PoseStamped, CARDSFlow_sending_data.robot_state_callback)
        rospy.Subscriber('/robot_state_target', PoseStamped, CARDSFlow_sending_data.robot_state_target_callback)
        
        rospy.Subscriber('/joint_state', JointState, CARDSFlow_sending_data.joint_state_callback)
        # not working 
        #rospy.Subscriber('/joint_state_target', JointState, CARDSFlow_sending_data.joint_state_target_callback)

        rospy.Subscriber('/tendon_state', Tendon, CARDSFlow_sending_data.tendon_state_callback)
        # not working
        #rospy.Subscriber('/tendon_state_target', Tendon, CARDSFlow_sending_data.tendon_state_target_callback)

        rospy.spin()


    except rospy.ROSInterruptException:
        pass
