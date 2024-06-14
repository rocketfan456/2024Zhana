
import #make sure you pull in numpy


# This function will output a summary of each phase
def PrintData(phaseList):
    print('{0:25s}'.format("------------------------------------------------------------------------" ))
    print('{0:20s}{1:>11s}{2:>11s}{3:>11s}'.format("Phase Name", "DV (m/s)", "Mass0 (kg)", "MassF (kg)" ))
    print('{0:25s}'.format("------------------------------------------------------------------------" ))
    for curPhase in phaseList:
        print('{0:20s}{1:11.1f}{2:11.1f}{3:11.1f}'.format(curPhase.strName ))

# This class will create a generic "phase" which will do propellant 
# calculations
class Phase:

    def __init__(self,strName, mStart, dvPhase, clsEng):

        # Check if this is a T/W phase. If so, 
        # update the dV calculate the thrust-to-weight
        twPhase = clsEng.thrust/(mStart*9.81)
        if dvPhase<0:
            dvPhase = #use the thrust-to-weight equation from the slides


        # Calculate Impulse Propellant Using Rocket Equation   
        # We specify Impulse because we'll have other types later
        mPropImpulse = 
   
        # Determine Oxidizer and Fuel
        mPropImpulseOx =
        mPropImpulseFuel =
        
          
        mEnd = mStart - mPropImpulse 
        
        
        # Move data to class structure to save information
        self.mStart         = mStart
        self.mEnd           = mEnd
        self.dvPhase        = dvPhase
        self.clsEng         = clsEng
        self.mPropImpulse   = 
        self.strName        = 
        self.twPhase        = 

        self.mPropImpulse   = 
        self.mPropImpulseOx =
        self.mPropImpulseFuel = 
 
# This class creates a summary of the entire mission - summing things up across
# phases         
class MissionSummary:
    def __init__(self, tupPhases):
        """
        Inputs:
            tupPhases: list of phase classes
        
        """
        # Initialize variables 
        mPropImpulse     = 0
        mPropImpulseOx   = 0
        mPropImpulseFuel = 0

        # sum up the usages by phase
        for curPhase in tupPhases:
            mPropImpulse     += curPhase.mPropImpulse 
            mPropImpulseOx   += 
            mPropImpulseFuel += 

        # Stuff everything into self    
        self.mPropImpulse      = mPropImpulse
        self.mPropImpulseOx    = 
        self.mPropImpulseFuel  = 


# This builds up an engine, with an assumed thrust, specific impulse, and 
# mixture ratio
class Engine:
    def __init__(self,isp, thrust, mr):
        self.isp = isp
        self.thrust = 
        self.mr = 

