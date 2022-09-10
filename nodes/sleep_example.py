import rospy

f = 1.0

# using rate.sleep():
rate = rospy.Rate(f)
while not rospy.is_shutdown():
    do_work()
    rate.sleep()

# using rospy.sleep( ):
while not rospy.is_shutdown():
    do_work()
    rospy.sleep(1. / f)
