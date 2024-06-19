# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:12:32 2020

@author: jlamp
"""
import numpy as np



def PrintData(phaseList):
    print('{0:25s}'.format("-----------------------------------------------------------------------------------------" ))
    print('{0:20s}{1:>11s}{2:>11s}{3:>11s}{4:>13s}{5:>13s}{6:>14s}'.format("Phase Name", "DV (m/s)", "Mass0 (kg)", "MassF (kg)", "TotProp (kg)", "OxProp (kg)", "FuelProp (kg)"  ))
    print('{0:25s}'.format("-----------------------------------------------------------------------------------------" ))
    for curPhase in phaseList:
        print('{0:20s}{1:11.1f}{2:11.1f}{3:11.1f}{4:13.1f}{5:13.1f}{6:14.1f}'.format(curPhase.strName, curPhase.dvPhase, curPhase.mStart, curPhase.mEnd, curPhase.mPropImpulse, curPhase.mPropImpulseOx, curPhase.mPropImpulseFuel ))

class Phase:

    def __init__(self,strName, mStart, dvPhase, clsEng):

        # Check if this is a T/W phase. If so, 
        # update the dV calculate the thrust-to-weight
        twPhase = clsEng.thrust/(mStart*9.81)
        if dvPhase<0:
            dvPhase = 4335*np.exp(-(twPhase)*20.25)+1880


        # Calculate Impulse Propellant Using Rocket Equation   
        mPropImpulse = mStart - mStart / np.exp(dvPhase/(9.81*clsEng.isp))

   
        # Determine Oxidizer and Fuel
        mPropImpulseOx = 
        mPropImpulseFuel = 
        
          
        mEnd = mStart - mPropImpulse 
        
        
        # Move data to class structure to save information
        self.mStart         = mStart
        self.mEnd           = mEnd
        self.dvPhase        = 
        self.clsEng         = 
        self.mPropImpulse   = 
        self.strName        = 
        self.twPhase        = twPhase

        self.mPropImpulse   = 
        self.mPropImpulseOx = 
        self.mPropImpulseFuel = 
          
class MissionSummary:
    def __init__(self, tupPhases):
        """
        Inputs:
            tupPhases: list of phase classes
        
        """

   
        
        mPropImpulse     = 0
        mPropImpulseOx   = 0
        mPropImpulseFuel = 0

        # sum up the usages by phase
        for curPhase in tupPhases:
            mPropImpulse     += curPhase.mPropImpulse 
            mPropImpulseOx   += 
            mPropImpulseFuel += 

        # Stuff everything into self    
        self.mPropImpulse      = 
        self.mPropImpulseOx    = 
        self.mPropImpulseFuel  = 



class Engine:
    def __init__(self,isp, thrust, mr):
        self.isp = 
        self.thrust = 
        self.mr = 

class TankSet:
    def __init__(self, strPropType,strMatType, nTanks, lMaxRadTank, presTank, mPropTotal):
        # General Parameters for Tanks
        pctUllage =          # Extra ullage room as a percentage of tank volume
        aMax      =           # Maximum acceleration (m/s2)
        pctFudge  =         # Fudge factor for welds, etc
        fosMat    =          # factor of safety for material (nd)
        
        # Tank material switch case
        if strMatType=="Al2219":
            rhoMat =      # Density of material (kg/m3)
            sigMat = 2.9e8    # Yield Stress of material (Pa)
            thkMin =    # Minimum thickness of material (m)
        elif strMatType=="Stainless":
            rhoMat = 8000
            sigMat = 
            thkMin = 0.0004
        elif strMatType == "Al-Li":
            rhoMat = 
            sigMat = 
            thkMin = 0.004
    
        
        # Propellant Density switch case
        if strPropType=="Oxygen":
            rhoProp =      # Density of propellant (kg/m3)
        elif strPropType=="Hydrogen":
            rhoProp = 
        elif strPropType == "Methane":
            rhoProp = 
        elif strPropType == "MMH":
            rhoProp = 
        elif strPropType == "NTO":
            rhoProp = 
        elif strPropType == "RP-1":
            rhoProp = 
        
        
        # Calculate propellant volume and volume per tank (include ullage)
        volPropTotal    = 
        volPropPerTank  = 
        volPerTank      = volPropPerTank*(1+pctUllage)
        
        # Compare volume of tank to maximum allowable for given radius
        #    This will help us determine if the tank is a sphere or a pill.
        volMaxRadius    = 4/3*np.pi*(lMaxRadTank**3)
        
        if volMaxRadius>volPerTank:
            # A sphere with the max radius is too big, so calculate
            # the needed radius and set cylinder length to zero
            lRadiusTank = (volPerTank*3/4/np.pi)**(1/3)
            lCylTank   = 0
            
        else:
            # A sphere with the max radius is too small, so calculate
            # what the cylinder length will be
            lRadiusTank = lMaxRadTank
            lCylTank    = (volPerTank-4/3*np.pi*(lRadiusTank**3))/(np.pi*lRadiusTank**2)
       
        # Calculate the total length of the tank 
        lTankLength = 
        
        # Calculate the surface area of each portion of the tank
        saDomesPerTank   = 4*np.pi*lRadiusTank**2
        saCylinderPerTank = 2*np.pi*lRadiusTank*lCylTank
        saTotalPerTank   = 
       
        # Calculate the thickness.  Start with pressure
        presTotal = fosMat*(presTank + rhoProp*aMax*lTankLength)
        thkDomesCalc  = 
        thkCylCalc    = 2*thkDomesCalc
        
        # Compare the pressure thickness to the minimum thickness
        thkDomes  = max(thkDomesCalc,thkMin)
        thkCyl    = 

        # Calculate the volume of the material
        volMatDomesPerTank = thkDomes*saDomesPerTank
        volMatCylPerTank   = 
        
        # Calculate the mass of each tank
        mDomesPerTank = volMatDomesPerTank*rhoMat
        mCylPerTank   = 
        
        # Add in the fudge factor 
        mTotalPerTank = 
        mTotal        = (mTotalPerTank*nTanks)*(1.1**nTanks)
        
       
       
       
        # Stuff everything back into "self" for output
        self.strPropType = strPropType
        self.strMatType  = 
        self.nTanks      = nTanks
        self.lMaxRadTank = lMaxRadTank
        self.presTank    = 
        self.mPropTotal  = mPropTotal
       
        self.pctUllage       = pctUllage
        self.rhoProp         = rhoProp
        self.volPropTotal    = 
        self.volPropPerTank  = volPropPerTank
        self.volPerTank      = 
        self.volMaxRadius    = volMaxRadius
        self.lRadiusTank     = 
        self.lCylTank        = lCylTank
        self.lTankLength     = 
        self.saDomesPerTank     = saDomesPerTank
        self.saCylinderPerTank  = 
        self.saTotalPerTank  = 
        self.presTotal       = 
        self.thkDomesCalc    = 
        self.thkCylCalc      = 
        self.thkDomes        = 
        self.thkCyl          = 
        self.volMatDomesPerTank = 
        self.volMatCylPerTank = 
        self.mDomesPerTank   = 
        self.mCylPerTank     = 
        self.mTotalPerTank   = 
        self.mTotal          = mTotal
