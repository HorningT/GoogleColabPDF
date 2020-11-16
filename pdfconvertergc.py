# -*- coding: utf-8 -*-
"""PDFconverterGC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EG4s-c-SqaoIIski6MaUWcNjsbldzYj9

# Converter from .ipynb to .pdf

# Version 1.4

### Converter
Save your .ipynb colab file into your Colab Notebooks folder in your Google Drive. 

[/content/gdrive/MyDrive/Colab Notebooks]()
"""

################################################################################
#                    CODE TO CONVERT COLAB NOTEBOOK TO PDF                     #
#This code converts an .ipynb file to a Tex based PDF and saves it in the Colab#
#Notebook folder with the same filename.pdf                                    #
################################################################################
# Function List PDFconvertGC(str(file location))
################################################################################

#Converter for .ipynb conversion to PDF. Input is a string of the file name
def PDFconvertGC(filename):
  # Imports
  from google.colab import drive; from datetime import datetime; import sys; 
  import os; import random; import time

  # Mount Drive First to give time for mounting to process
  drive.mount('/content/gdrive', force_remount = True) 

  # Install some dependences into the RUNTIME (is not local, needs to reinstall 
  # every Factory runtime)
  t1 = time.time()
  os.system('pip install IPython >> outputsuppressed.txt')
  os.system('pip install Latex >> outputsuppressed.txt')
  os.system('pip install pandoc >> outputsuppressed.txt')
  os.system('install nbconvert >> outputsuppressed.txt')
  os.system('pip install jupyter >> outputsuppressed.txt')
  os.system('apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended >> outputsuppressed.txt')
  t2 = time.time(); m = str(int((t2-t1)/60)); s = str(int((t2-t1)% 60))
  print("Install Time: ",m," m  ",s," s")

  # Searches the Google drive directory for the filename and gives back it's 
  # location (This accounts for Wildcards and Spaces in the directory names).
  # Uses jupyter and nbconvert to convert to a Tex file, then into a pdf 

  # Handle Common Errors
  try:
    print('\nFinding file. This may take a minute or two depending on the size of your drive...\n')
    os.system("IFS=$'\n'") #Sets the reader to only break at newlines instead of spaces, tabs,and newlines
    loc = os.path.abspath(filename)
  except IndexError as error:
    print(color.BOLD,color.FAIL, "\nCould not find file in your Drive!\n" 
          ,color.END,color.WARNING
          ,"- Make sure you input the correct filename\n"
          ,"  - Make sure the file is saved in the google drive you mounted\n\n"
          ,color.END)
    Er = str('Error: {}. {}, line: {}'.format(sys.exc_info()[0],sys.exc_info()[1]
                                            ,sys.exc_info()[2].tb_lineno))
    f = open("ErrorLog.txt","a+"); f.write(Er); f.close()
    sys.tracebacklimit=0
    sys.exit("Please Try Again") 
  except Exception as exception:
    print(color.BOLD,color.WARNING, "Exception Occured, Please Check Log",color.END)
    Er = str('Error: {}. {}, line: {}'.format(sys.exc_info()[0],sys.exc_info()[1]
                                              ,sys.exc_info()[2].tb_lineno))
    f = open("ErrorLog.txt","a+");f.write(Er);f.close()
    sys.tracebacklimit=0
    sys.exit("Please Try Again")
  print('File Location: ',str(loc),'\n')
  t3 = time.time(); 
  m = str(int((t3-t2)/60)); 
  s = str(int((t3-t2)% 60))
  print("Search Time: ",m," m  ",s," s")

  # Autosave file
  os.system('sleep 60s')

  # Convert the file
  os.system('jupyter nbconvert --to pdf "{fileloc}" --log-level ERROR')
  # The PDF will be in the same folder as the original file
  print(color.GREEN,"Conversion Complete!\nGreat Job and Have a Wonderful Day!"
      ,color.END,"\U0001F30C")
  t4 = time.time(); 
  m = str(int((t4-t3)/60));
  s = str(int((t4-t3)% 60))
  print("Conversion Time: ",m," m  ",s," s")
  m = str(int((t4-t1)/60)); 
  s = str(int((t4-t1)% 60))
  print("Total Time: ",m," m  ",s," s")

def Watermark(filename):
  from datetime import datetime;
  # To make Watermark distinctive
  class color:
    BLUE = '\033[94m';
    GREEN = '\033[92m';
    BOLD = '\033[1m';
    UNDERLINE = '\033[4m';
    END = '\033[0m';
    FAIL = '\033[91m';
    WARNING = '\033[93m'

  # Make Watermark
  now = datetime.now()
  print(color.UNDERLINE,'Unique Watermark\n',color.END)
  print(color.BOLD,color.BLUE, str(filename),'\U0001F512\n',color.END)
  print(color.BOLD,color.BLUE,now.strftime("%d/%m/%Y %H:%M:%S")," "
      ,str(random.randrange(1000000, 9999999, 1)),color.END,'\n')


############ Version Control:
# Last Update: 2020-10-18, 1459 - V 1.4.1 - Thomas Horning
# - Error Handling
# - Autosave added before conversion so that watermark is gaurenteed
# - Added timers for debugging
# Created by Thomas Horning

"""###Current Common Errors
- Not handling spaces. Rename with no (1)
  - Usually Gives a LaTex Error
- Not handling Images of any kind
 - Built-in insert image breaks conversion
   - ![something]{something}

###Developer Notes
 - There are many redundant installs in the beginning. This is because it works, and I am scared to touch it
 - I run into Excessive search time issues on a 65 Gb Drive. 
"""
