#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

class Adder(object):
    def __init__(self):
        self.sum = 0
        self.sub = rospy.Subscriber("number", Float64, self.callback)

    def callback(self, msg):
        self.sum += msg.data
        print("The sum is now {}".format(self.sum))

rospy.init_node("adding_node")
adder = Adder()
rospy.spin()

