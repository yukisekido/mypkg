# SPDX-License-Identifier: BSD-3.0

#Copyright (C) 2021 Yuki Sekido and Ryichi Ueda. All rights reserved.

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data**2

rospy.init_node('square')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('square', Int32, queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
