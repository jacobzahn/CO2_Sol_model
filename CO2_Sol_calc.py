#---------------------------------------------------------------------------
# 4/16/17
# Author: Jacob Zahn
# Calculating CO2 and Solar Forcings over Earth's History
#---------------------------------------------------------------------------

# Those Sweet Imports
#---------------------------------------------------------------------------
import numpy as np
import CO2_Sol_globals as gl
#---------------------------------------------------------------------------

# Calculating Forcings
#---------------------------------------------------------------------------
class CO2_Forcing(object):

    def __init__(self,C0,C):
        self.aa = np.log(gl.C0**-1*gl.C)        # First term in CO2 Forcing
        self.bb = (np.log(gl.C0**-1*gl.C))**2   # Second Term in CO2 Forcing
        self.dFCO2 = 5.32*self.aa+0.39*self.bb  # CO2 Forcing [W/m2]
    
class Solar_Forcing(object):

    def __init__(self,Fst,Fs,A):
        self.dFSol = ((gl.Fst-gl.Fs)*(1-gl.A))/4    # Radiative Forcing [W/m2]

for ii in range(len(gl.C)):
    gl.Fst[ii] = gl.Fs/(1+(0.4*(1-gl.t0**-1*gl.t[ii])))
    gl.dFCO2[ii] = CO2_Forcing(gl.C0,gl.C).dFCO2[ii]
    gl.dFSol[ii] = Solar_Forcing(gl.Fst,gl.Fs,gl.A).dFSol[ii]
    gl.dF[ii] = gl.dFCO2[ii]+gl.dFSol[ii]
#---------------------------------------------------------------------------