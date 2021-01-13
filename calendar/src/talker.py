#!/usr/bin/env python
# license removed for brevity
import rospy
import string
import datetime
import random
from std_msgs.msg import String
from std_msgs.msg import Bool


def talker():
    pub = rospy.Publisher('day', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        msg = String()
	d = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
     '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
	m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
	msg.data = random.choice(d) + '.' + random.choice(m)
        rospy.loginfo('sended data: {msg.data}')
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

