# SPDX-License-Identifier: BSD-3.0

#Copyright (C) 2021 Yuki Sekido. All rights reserved.

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*10

rospy.init_node('tentimes')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('tentimes', Int32, queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()

