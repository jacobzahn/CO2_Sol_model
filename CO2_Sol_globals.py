#---------------------------------------------------------------------------
# 4/18/17
# Author: Jacob Zahn
# Global Variables for CO2 & Solar Forcing Model
#---------------------------------------------------------------------------

# Those Sweet Imports
#---------------------------------------------------------------------------
import numpy as np
#---------------------------------------------------------------------------

# Defining Constants & Variables
#---------------------------------------------------------------------------
x = 1                            # Timestep
t = np.arange(4170,4570,x)       # Time Array
Fs = 1368                        # Present-day Total Solar Irradiance [W/m2]
A = 0.3                          # Average Albedo of Earth
t0 = 4570                        # Age of the Earth [Myrs]
C0 = 278                         # Pre-Industrial CO2 [ppm]
C = np.arange(400,2000,4)        # Approximate CO2 Record (len(t) = len(C))
C = C[::-1]                      # Reorienting CO2 Array
dFCO2 = np.zeros(len(t))         # Initializing CO2 forcing Array
dFSol = np.zeros(len(t))         # Initializing Solar forcing Array
dF = np.zeros(len(t))            # Initializing Combined forcing Array
Fst = np.zeros(len(t))           # TSI over last 400 [W/m2]
#---------------------------------------------------------------------------