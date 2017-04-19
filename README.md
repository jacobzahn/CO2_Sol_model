# CO2_Sol_model

This model uses a simplified CO2 record to construct the CO2 radiative forcing for Earth, and compares it to solar forcing 
over the same time period.

# There are three modules involved in this model:

# A) CO2_Sol_main.py
This is the main module, and the one you will run. It imports the other modules, and then plots the results.

# B) CO2_Sol_globals.py
This module initializes the constants and variables that will be used in the model. These can be changed to fit the experiment.

# C) CO2_Sol_calc.py
This module calcuates the Solar and CO2 forcings, which are then plotted against time in CO2_Sol_main.py.

# How to run the model
To run this model, first make sure all three of the above files are in your working directory. Then in ipython or whichever interface you use, type "run CO2_Sol_main.py". The output will be one plot that shows Solar Forcing, CO2 Forcing, and their sum over the time period of interest.
