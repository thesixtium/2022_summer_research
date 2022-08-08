README.TXT - File list and instructions for installation of the SRS RGA LabVIEW
Development Kit.

FILE LISTING
-------------------------------------------------------------------------------
Appendix_d.doc                                  Appendix to RGA manual
README.TXT                                      This File, ASCII format
SRSRGA85.llb                                    Library file for LabVIEW 8.5

INSTALLATION INSTRUCTIONS
-------------------------------------------------------------------------------
IMPORTANT:  This distribution of the SRS RGA Development Kit is for use with
LabVIEW 8.5.  This kit has been tested its compatiblity with Labview 12.0 (32 bit).

The "installation" consists of simply copying the SRSRGA85.llb file to
a directory you wish to use.

This version includes two communication connections; Serial & Ethernet.  
For Ethernet connection, a customer should have an RGA Ethernet adapter (REA) from
SRS.  Please refer to REA manual for the details of Ethernet parameter settings.


WARNING!
Changing the gain of the electron multiplier without changing its
high voltage setting will ruin your calibration.  If you wish to
increase the gain, raise the high voltage setting and set the gain
to 1.  Run a scan in faraday cup mode and in electron multiplier
mode, noting the signal value for a peak in both modes.  The ratio
of the peak value between the two modes is the gain factor.  Return
to the detector setup and set the gain factor to this value.  See
appdenix_d.doc and your RGA manual (page 7-14) for details.
WARNING!

Appendix_d.doc is a detailed document designed to be an appendix to your RGA
Manual.  It contains very helpful information on the architecture of the
drivers and their use.  Please read it BEFORE you begin development.

NOTE:  SRS does not support LabVIEW.  These drivers are provided at no
cost, and AS IS.  Do not contact SRS with questions on LabVIEW.  To learn
LabVIEW programming techniques, contact National Instruments, Incorporated
at 512-794-0100 or visit their web site, www.ni.com.
