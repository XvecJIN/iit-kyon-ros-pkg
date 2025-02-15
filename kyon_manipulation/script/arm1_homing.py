#!/usr/bin/env python3

from cartesian_interface.pyci_all import *
import rospy
import numpy as np
from scipy.spatial.transform import Rotation

rospy.init_node('test')

cli = pyci.CartesianInterfaceRos()
task_name = 'dagana_1_base'
arm1 = cli.getTask(task_name)

cli.update()

Tref, _, _ = arm1.getPoseReference()
print(Tref)


waypoints = []

wp = pyci.WayPoint()
wp.frame.translation = [0.1487, 0.2165, 0.5238]
wp.frame.quaternion = [ 0.02462,   0.1736,   0.9845, 0.004341]
wp.time = 5.0
waypoints.append(wp)

arm1.setWayPoints(waypoints)
arm1.waitReachCompleted(10.0)
