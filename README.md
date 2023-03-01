# CWRS_SHAW
Data processing, input file generation for SHAW and batch processing of SHAW jobs.

SHAW_weaFile.py is meant to  process and weather input files downloaded from Environment Canada via Cygwin and NASA POWER and combine them into the .wea file format SHAW is looking for.

SHAW_batchProc.py is meant to run SHAW multiple times for different cases.

The script works as follows:

It iterates over the trials, first moving the input files into the working directory.
Then, it runs Shaw302.exe with the input files.
Next, it moves the input files out of the working directory back into the folder they came from.
Finally, it moves the output files into a newly-created folder, removing the old one if present.

The srcipt is designed with the following file structure in mind:

[overall folder]
--protocol.xlsx
--[working directory]
----SHAW_batchProc.py
----Shaw302.exe
----[Inputs]
------[Trial001]
------[Trial002]
------[Trial...]
----[Outputs]
------[Trial001]
------[Trial002]
------[Trial...]
