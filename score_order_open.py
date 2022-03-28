import os
import fnmatch
import glob
import pprint
import json
import subprocess
import webbrowser





#for file in glob.glob("clarinet"):
    #print(file)





#/Users/drakedomingue/Desktop/Part PDFs/Lizzie and Lucy PARTS/Lizzie and Lucy PDF Parts/Lizzie and Lucy  - Trombone 1.pdf

#substring_in_list = any(horn in part_pdf for part_pdf in horn)





# Creates variable to grab every PDF file in the main directory/sub directories

#Lizzie and Lucy
directory = '/Users/drakedomingue/Desktop/Part PDFs/Lizzie and Lucy PARTS/'
sub_directory = '/Users/drakedomingue/Desktop/Part PDFs/Lizzie and Lucy PARTS/Lizzie and Lucy PDF Parts/'

#Twilight Waltz

#directory = '/Users/drakedomingue/Desktop/Part PDFs/49519 - YS - Twilight Waltz'
#sub_directory = '/Users/drakedomingue/Desktop/Part PDFs/49519 - YS - Twilight Waltz/49519_ENG_PDF'

part_pdf = glob.glob(f"{directory}/**/*.pdf", recursive = True)
part_pdf_please = glob.glob(f"{sub_directory}/**/*.pdf", recursive = True)

os.chdir(directory)




#for filename in part_pdf:
    #os.system(filename)
    #subprocess.Popen(filename, shell=True)

    #print(filename)
    #os.system(filename)
    #subprocess.Popen(filename, shell=True)


#Creates list of all PDFS without file path. Not functional yet when working with files

for part in part_pdf:
    edit_part = [part[106:] for part in part_pdf]

#Function that finds woodwind PDFs in a directory
def find_woodwinds():
    flute = [match for match in part_pdf if "Flu" in match]
    oboe = [match for match in part_pdf if "Ob" in match]
    bassoon = [match for match in part_pdf if "Bassoon" in match]
    clarinet = [match for match in part_pdf if "Clar" in match]
    sax = [match for match in part_pdf if "Sax" in match]

    wws = []

    for winds in flute:
        wws.append(winds)
    for winds in oboe:
        wws.append(winds)
    for winds in bassoon:
        wws.append(winds)
    for winds in clarinet:
        wws.append(winds)
    for winds in sax:
        wws.append(winds)

    return wws

woodwind_print = find_woodwinds()

#print(woodwind_print)


#for files in directory:
#    wws_2 = []
#    if files in woodwind_print:
    #    wws_2.append(winds)

wws2 = list(set(part_pdf).intersection(set(woodwind_print)))

print(wws2)

#webbrowser.open_new(part_pdf[0])
#subprocess.Popen(part_pdf[0], shell=True)
#os.system(part_pdf[3])






#for part in edit_part:
