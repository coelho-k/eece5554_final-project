#!/usr/bin/env python
import roslib
import rospy
import tf
from sensor_msgs.msg import NavSatFix
import sys
import re
import datetime
import calendar
import math
import logging
import gps_converter


# all arrays are in the following format
# [easting northing]
startEN = [-1, -1]
currEN = [-1, -1]

def tfHandler(data):
    global startEN
    global currEN
    rospy.loginfo('I heard GPS')
    if (startEN[0] == -1 and startEN[1] == -1):
        startEN = convertToUTM(data)
        
    currEN = convertToUTM(data)
    
    eastDiff = currEN[0] - startEN[0]
    northDiff = currEN[1] - startEN[1]

    br = tf.TransformBroadcaster()
    br.sendTransform((eastDiff, northDiff, 0.0),
                     (0.0, 0.0, 0.0, 1.0),
                     rospy.Time.now(),
                     "base_footprint",
                     "world")
    rospy.loginfo('I sent a transform [' + str(eastDiff) + ', ' + str(northDiff) + ']')

# to convert the NavSatFix data to utm coordinates
def convertToUTM(gps_data):
    values = [-1, -1]
    convert_result = gps_converter.from_latlon(gps_data.latitude, gps_data.longitude)
    values[0] = convert_result[0] # easting
    values[1] = convert_result[1] # northing 
    return values


if __name__ == '__main__':
    rospy.init_node('world_pub', anonymous=True)
    rospy.Subscriber("/vehicle/gps/fix", NavSatFix, tfHandler)
    rospy.loginfo('Starting World Publisher')
    rospy.spin()
