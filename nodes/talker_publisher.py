#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node("talker", anonymous=True)
pub = rospy.Publisher("chatter", String, queue_size=10)
rospy.sleep(1.0)

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    msg = String()
    msg.data = "hello world"
    pub.publish(msg)
    rate.sleep()
