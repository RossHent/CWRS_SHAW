#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%% Created February 17, 2023
#%% Author: Ross Henteleff

import subprocess as sp
import os
import pandas as pd
import glob
import shutil

#%% Reading in protocol
protocol = pd.read_excel(r'C:\Users\uOttawa\Desktop\DAL\SHAW\protocol.xlsx', header=1)

#%% Setting working directory to where Shaw302.exe is located
path = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs"

os.chdir(path)

#%% Locating input and output file folders and getting list of trials to be run
inputPath = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs\Inputs"
outputPath = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs\Outputs"

suff_inp = ".inp"

dirs = os.listdir(inputPath)

for trial in dirs:
    
    #%% Locating particular trial to be run
    trialPath_inp = inputPath + "\\" + trial
    
    #%% Moving input files into working directory
    globInp_path_in = trialPath_inp + "\\" + trial   ##Describing the input file name pattern
    inputs_in = glob.glob(globInp_path_in + "*")     ##Creating a list of the input files
    
    for file in inputs_in:   ##Moving the input files into the working directory
        source_in = file
        destination_in = path
        shutil.move(source_in, destination_in)

    inputs_in.clear()   ##Clearing the list to be used in the next loop iteration
    
    #%% Locating and running the .exe
    exe = path + "\\" + "Shaw302.exe"   ##Describing the .exe location
    inp = trial + suff_inp + '\n'      ##Creating the string input file input
    p = sp.Popen(exe, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, encoding="UTF8")
    p.stdin.write(inp)
    p.stdin.flush()
    p.wait()
    
    #%% Moving the input files out of the working directory
    globInp_path_out = path + "\\" + trial           ##Describing the input file name pattern
    inputs_out = glob.glob(globInp_path_out + "*")   ##Creating a list of the input files
    
    for file in inputs_out:   ##Moving the input files out of the working directory
        source_out = file
        destination_out = trialPath_inp
        shutil.move(source_out, destination_out)
    
    inputs_out.clear()   ##Clearing the list to be used in the next loop iteration
    
    #%% Checking if output folder exists, if so deleting it and creating a new output folder
    trialPath_out = outputPath + "\\" + trial   ##Getting the name of the output folder
    
    if os.path.exists(trialPath_out):   ##Checking if the output folder exists
        shutil.rmtree(trialPath_out)    ##Deleting it if so
    
    os.mkdir(trialPath_out)             ##Creating a new output folder
    
    #%% Moving the output files into the output folder
    out_ptn = "\*.out"                    ##Describing the output file name pattern
    outputs = glob.glob(path + out_ptn)   ##Creating a list of the output files
    
    for file in outputs:   ##Moving the output files out of the woking directory
        outName = os.path.basename(file)
        shutil.move(file, trialPath_out + '\\' + outName)
        
    outputs.clear()   ##Clearing the list to be used in the next loop iteration


# In[ ]:





# In[ ]:




