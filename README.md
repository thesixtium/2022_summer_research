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
There was a linear tribometer already set up in the Nanotribology lab, and some mechanical work had been done by a previous research assistant towards making it circular. All the mechanical had already been set up, so it was mostly assembling it, adjusting parts, and making the software.

### Link to GitHub
You can find the project-specific GitHub here:
[thesixtium/rotating_grease_tribometer](https://github.com/thesixtium/rotating_grease_tribometer)

### What's Been Done
* All the mechanical has been figured out and assembled
* Calibration files and software have been found, loaded, and run
* The control software has been created in LabVIEW by adapting parts from other part-specific control softwares
* All of the electrical wiring has been cleaned up (removing useless wires, cable management, etc.).

### What Needs to Happen
* The software made is only a foundation, versions of this foundational software need to be made and modified to automatically run specific experiments.

### Documentation
* The LabVIEW software contains documentation and labelling within it.
* There is also a supporting powerpoint in the project-specific GitHub.

### Links
[Thesis paper this was based on](https://www.ucalgary.ca/sites/default/files/teams/135/Brandon%20Wong%20MSc%20Thesis.pdf)

[Mini40 Info](https://www.ati-ia.com/products/ft/ft_models.aspx?id=mini40)

[DMX-J-SA-17 Drivers](https://www.arcus-technology.com/support/downloads/download-category/software-installation/)

[DriveMax Series Software](https://www.arcus-technology.com/support/downloads/download-info/drivemax-series-installer/)

[Drivers and Tools Installer](https://www.arcus-technology.com/support/downloads/download-info/drivers-and-tools-installer/ )

## Atomic Force Microscopy Remote Control
The goal of the AFM Remote Control was to be able to control the AFM remotely and access all data from the desktop instead of needing to read stuff off of the attached machines. The AFM is actually a combination of different modules, and I focused on the PreVac units, and specifically the BCU-14.

### What's Been Done
* PreVac turned out to actually have prebuilt software for controlling their units, so finding the software was step 1
* I then figured out how to set up the prebuilt software, and specifically how to run it over ethernet.

### What Needs to Happen
* Lots of links on PreVac’s site are broken / contain incorrect information, making it hard to get all the software needed for integration and other modules. This needs to be fixed somehow.
* The Prevac software needs to be integrated with the existing AFM LabVIEW code
* Figure out how to integrate the non-PreVac modules, and hopefully find more prebuilt software (if not, will need to build some).

### Documentation
* Slide 10 on the powerpoint in this repository is on Heat3.exe Setup instructions. Should be the same procedures for all PreVac stuff
* Below there is also a link with documentation


### Links
[Downloads](https://www.prevac.eu/en/c,6,download.html)

[Firmware](https://moplink.prevac.pl/fsdownload/DOnc5VJEi/Firmware)

[Software](https://moplink.prevac.pl/fsdownload/aSfFCUArk/Customer_Download)

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