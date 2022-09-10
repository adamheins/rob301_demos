#!/usr/bin/env python
import rospy

rospy.init_node("talker", anonymous=True)

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rospy.loginfo("hello world")
    rate.sleep()

# What happens if we use `while True` instead of
#   `while not rospy.is_shutdown()`?
# What happens if we omit `rate.sleep()`?
# What happens if `anonymous=False`?
