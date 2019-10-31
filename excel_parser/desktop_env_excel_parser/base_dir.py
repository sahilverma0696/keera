# first script to be executed to set the directories for the user 

from os import makedirs, path

if not path.exists(path.expanduser("~/Desktop/Spacemonk/input")):
    makedirs(path.expanduser("~/Desktop")+"/Spacemonk/input")
    print("Folder created, please put the data")
else:
    print("Input Folder exits")

if not path.exists(path.expanduser("~/Desktop/Spacemonk/output")):
    makedirs(path.expanduser("~/Desktop")+"/Spacemonk/output")
    print("Output folder created.")
else:
    print("Output Folder exists")