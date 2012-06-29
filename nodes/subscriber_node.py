#!/usr/bin/env python
import roslib
roslib.load_manifest('spheretrax_example_subscriber')
import rospy

from spheretrax_ros.msg import SphereTraxData

class SubscriberNode(object):

    def __init__(self):

        rospy.init_node('example_subscriber')
        self.sub = rospy.Subscriber('/spheretrax/data',SphereTraxData,self.handle_data)

    def run(self):
        rospy.spin()

    def handle_data(self,data):
        print data
        print

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    node = SubscriberNode()
    node.run()
