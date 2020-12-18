import rospy
import datetime
from std_msgs.msg import String
from std_msgs.msg import Bool

def calendar(data):
    pub = rospy.Publisher('is_holiday', Bool, queue_size=10)
    rospy.loginfo(f'Selected date: {data.data}')
    msg = Bool()
    holiday_2020 = {'01.01', '02.01', '03.01', '04.01', '05.01', '06.01', '07.01', '08.01',
                    '11.01', '12.01', '18.01', '19.01', '25.01', '26.01', '01.02', '02.02',
                    '08.02', '09.02', '15.02', '16.02', '22.02', '23.02', '24.02', '29.02', '01.03',
                    '07.03', '08.03', '09.03', '14.03', '15.03', '21.03', '22.03', '28.03', '29.03', '04.04', '05.04',
                    '11.04', '12.04', '18.04', '19.04', '25.04', '26.04', '01.05', '02.05', '03.05', '04.05', '05.05',
                    '09.05', '10.05', '11.05', '16.05', '17.05', '23.05', '24.05', '30.05', '31.05',
                    '06.06', '07.06', '12.06', '13.06', '14.06', '20.06', '21.06', '27.06', '28.06',
                    '04.07', '05.07', '11.07', '12.07', '18.07', '19.07', '25.07', '26.07', '01.08', '02.08',
                    '08.08', '09.08', '15.08', '16.08', '22.08', '23.08', '29.08', '30.08', '05.09', '06.09', '12.09',
                    '13.09', '19.09', '20.09', '26.09', '27.09', '03.10', '04.10', '10.10', '11.10', '17.10',
                    '18.10', '24, 10', '25.10', '31.10', '01.11', '04.11', '07.11', '08.11', '14.11', '15.11', '21.11',
                    '22.11',
                    '28.11', '29.11', '05.12', '06.12', '12.12', '13.12', '19.12', '20.12', '26.12', '27.12'}
    if data.data in holiday_2020:
        msg.data = True
    else:
        msg.data = False
    rospy.loginfo(f'Is a holiday?: {msg.data}')
    pub.publish(msg)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('day', String, calendar)
    rospy.spin()

if __name__ == '__main__':
    listener()
