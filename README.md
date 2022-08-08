# Summer Research Culmination

This is a detailed breakdown of my research work at the [Nanotribology Lab](https://www.ucalgary.ca/labs/nanotribology) as part of the **Egberts Research Group** at the University of Calgary during the spring and summer semesters. 

## Overview

These are the following things I worked on over the research term:
* Bearing Vibration Analysis Setup
* Circular grease Tribometer
* Atomic Force Microscopy Remote Control
* Atomic Force Microscopy Peak Detection
* Atomic Force Microscopy Tip Holders

## Bearing Vibration Analysis Setup
I worked on the electrical and software design for this project. It is *extremely* loosely based on the setup shown in "A Novel Tribometer Designed
to Evaluate Geological Sliding
Contacts Lubricated by Drilling Muds" in the Journal of Testing and Evaluation, published by Philip Egberts, Nicholas Simin, Calvin Wong, Jan Czibor, Curtis Ewanchuk, and Simon Par.

The goal of this project is to research faults in bearings, and see if specific vibrations can be recorded to predict not only a fault in a bearing ahead of time but also what the fault is caused by.

The two main parts of this project was electrically connecting everything properly, and then coding everything to work. The main electrical parts are:
* NI myDAQ
* AC Motor
* Torque Sensor
* AC Motor PSU
* Torque Sensor PSU

The electrical was mostly just wiring connections between different parts, however, an opamp had to be wired and installed to allow a voltage range expansion on the controlling DAQ.

The software was all done in LabVIEW and was focused on getting the torque sensor to act in a feedback loop with the motor in order to control the motor's speed.

I made good progress on this project, but there was just not enough time to finish it during my summer term.

### Link to GitHub
You can find the project-specific GitHub here:
[thesixtium/Bearing_Vibration_Analysis_Setup](https://github.com/thesixtium/Bearing_Vibration_Analysis_Setup)

### What's Been Done
* The electrical schematics were made according to specifications by the head Ph.D. student. 
* Version 1 of the electrical setup was tested. It didn’t reach the full 42V range because of an oversight in the opamp chip (although rated to go to a full 42V, it only had a gain of 5V). Everything else worked through.
* Version 2 of the electrical was tested. Everything seemed to work, but because the opamp came in a smaller package than expected (TSSOP) and because the protoboard was being soldered by hand, this lead to a short that caused the board to fail.

### What Needs to Happen
* The protoboard that is the current circuit needs to be redone to fix the solder. Instead of ordering more parts and trying to do everything by hand, I would recommend making an actual PCB for it. The protoboard was only tried because it was faster and guaranteed to give me enough time for 2 attempts and was easy to resolder parts if needed. Redo circuit board, probably print an actual PCB
* Range scaling and calibration need to be added to the LabVIEW program to allow for easier control of the motor feedback loop. Currently, the numbers are not mapped to any understandable value and are pretty arbitrary outside of having a mix between a logarithmic and linear relationship with the motor's speed.
* The integration of the accelerometers and brake integration needs to be done, they weren't a priority at the start of this project for electrical so they were largely ignored.

### Documentation
All the needed documentation is on the project's GitHub, with “Bearing Information.pptx” being the most up-to-date and informative file on everything. There is also a bunch of supporting documentation.

## Circular grease Tribometer
Overview
### Link to GitHub
### What's Been Done
### What Needs to Happen
### Documentation
### Links

## Atomic Force Microscopy Remote Control
Overview
### Link to GitHub
### What's Been Done
### What Needs to Happen
### Documentation
### Links

## Atomic Force Microscopy Peak Detection
This code is meant to automate the process of finding peaks and valleys in AFM data and do all the needed math, turning hours or days of work into under a minute of computing. 
### Link to GitHub
You can find the project-specific GitHub here:
[thesixtium/AFM_Peak_Detection](https://github.com/thesixtium/AFM_Peak_Detection)

### What's Been Done
* The base code has been made, tested, and tuned on one dataset. 
* It has also run and is confirmed to work on a second dataset.

### What Needs to Happen
* There needs to be more testing and adjustments on other datasets.
* All the magic numbers should be automatically generated from the dataset instead of having to be tested and manually made.
* The software needs to be applied.

### Documentation
There is extensive documentation on GitHub and throughout the code, which should make everything clear. 

## Atomic Force Microscopy Tip Holders
I got asked to make holders for the AFM tips; I have no idea what they are used for or why they are needed.

### Link to GitHub
You can find the project-specific GitHub here:
[thesixtium/Vinay_Tip_Holders](https://github.com/thesixtium/Vinay_Tip_Holders)
### What's Been Done
* They were made, printed, and verified to work

### Documentation
The STL file is on the GitHub link, nothing else to document.

## License
[MIT](https://choosealicense.com/licenses/mit/)