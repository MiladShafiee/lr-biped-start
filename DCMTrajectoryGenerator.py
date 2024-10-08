import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

class DCMTrajectoryGenerator:
    def __init__(self,CoMHeight):
        self.CoMHeight = CoMHeight # We assume that CoM and pelvis are the same point
        self.timeStep = 1.0/240.0 #We select this value for the timestep(dt) for discretization of the trajectory. The 240 Hz is the default numerical solving frequency of the pybullet. Therefore we select this value for DCM trajectory generation discretization. Note that the toy example will have a different time-step of 0.001.
        self.DCM = ([0.0,0.0])
        self.CoP = ([0.0,0.0])
        self.CoMDot = np.array([0.0,0.0])
        self.CoM = np.array([0.0,0.0])
        self.CoMDotPrev = np.array([0.0,0.0])
        self.initialDCM = np.array([0. , 0.])
        self.gravityAcceleration = 9.81
        self.omega = math.sqrt(self.gravityAcceleration/self.CoMHeight ) #Omega is a constant value and is called natural frequency of linear inverted pendulum
        pass


    def getDCMTrajectory(self,time): # Here we call planDCMTrajectory and we get DCM
        self.planDCMTrajectory(time) #Plan DCM trajectory 
        return np.array(self.DCM)


    def getCoM(self):
        #This function generates the CoM trajectory by integration of CoM velocity(that has been found by the DCM values)
        self.CoMDot= self.omega * (self.DCM - self.CoM) # TODO: use equation (3) in the project description
        self.CoM = self.CoM + self.CoMDot * self.timeStep# TODO: Simple euler numerical integration
        self.CoMDotPrev=self.CoMDot
        return self.CoM

    
    def planDCMTrajectory(self,time): #The output of this function is DCM posiiton
        #TODO: use the equation 9 of the project description
        self.DCM = (self.initialDCM - self.CoP) * np.exp(self.omega * self.timeStep) + self.CoP # TODO
        # [NOTE] The DCM there should be the exactly initial state (initialDCM), instead of the DCM of previous timestep.
        pass

    


    


