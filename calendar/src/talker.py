#!/usr/bin/env python
# license removed for brevity
import rospy
import string
import datetime
from std_msgs.msg import String
from std_msgs.msg import Bool


def talker():
    pub = rospy.Publisher('day', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        msg = String()
        if datetime.datetime.strptime(msg.data, "%d.%m"):
            rospy.loginfo(f'sended data: {msg.data}')
        else:
            return None
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
