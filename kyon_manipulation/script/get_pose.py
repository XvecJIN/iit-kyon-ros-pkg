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