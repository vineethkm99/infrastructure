#This program sorts the files on Desktop on the basis of file extension and move them in separate folders in Documents folder.

desktop_directory="/home/vineeth/Desktop/" #LINUX
destination_folder="/home/vineeth/Documents/" #LINUX

#desktop_directory="C:/Users/VINEETH/Desktop/" #Windows
#destination_folder="C:/Users/VINEETH/Documents/" #Windows

exclude_these = ['.desktop','.exe','.lnk']
import os
for eachfile in os.listdir(desktop_directory):
    if os.path.isfile(desktop_directory+eachfile):
        fileName, fileExtension = os.path.splitext(eachfile)
        if(all(fileExtension!=e for e in exclude_these)):
            ext=fileExtension[1:]
            if not os.path.exists(destination_folder+ext):
                os.mkdir(destination_folder+ext)
            os.rename(desktop_directory+eachfile,destination_folder+ext+"/"+eachfile)
