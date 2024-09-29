import numpy as np
import math
from matplotlib import pyplot as plt

class FootTrajectoryRecovery:
    def __init__(self, stepTime, maximumStepHeight):
        self.tStep_ = stepTime
        self.dt_ = 1/240
        self.leftFirst_ = True
        self.height_ = maximumStepHeight
        pass


   
    def getSwingFootTrajectory(self,footPoseStart,footPoseEnd,time):
        coefs = self.polynomial(footPoseStart[0],footPoseEnd[0], self.height_,self.tStep_-self.tDS_*.0)
        footPosition = coefs[0] + coefs[1] * time + coefs[2] * time**2 + coefs[3] * time**3 + coefs[4] * time**4 + coefs[5] * time**5                                
        return footPosition

    def polynomial(self,x0, xf, z_max, tf):
        ans = list("")
        ans.append(x0)
        ans.append(np.zeros(3))
        ans.append(np.zeros(3))
        ans.append(10/tf**3 * (xf - x0))
        ans.append(-15/tf**4 * (xf - x0))
        ans.append(6/tf**5 * (xf - x0))

        ans[0][2] = 0.0
        ans[1][2] = 0.0
        ans[2][2] = 16 * z_max / tf**2
        ans[3][2] = -32 * z_max / tf**3
        ans[4][2] = 16 * z_max / tf**4
        ans[5][2] = 0.0

        return ans 
