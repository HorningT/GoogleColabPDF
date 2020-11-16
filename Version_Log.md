
# <font size="6">**Version Log**</font>


###Usage Information
- <font size="2">Change to V 1.(n+1) for every update that makes it into a student version</font>
- <font size="2">Make a new markdown cell for each Update and follow the  established format</font>
- <font size="2">If code is added, place the code in the update </font>

##1.4 (Thomas Horning, 1434, 18 October 2020)

*Changes:*
- Collapsed Student Version so it takes less space for them.
 - Same amount on pdf unfortunately

- Reformatted code for readability and useability

- Added color class in order to better distinguish the output of the watermark and errors
 - ```
class color:
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
print(color.UNDERLINE,'Unique Watermark',color.END,'\U0001F512\n',color.END)
print(color.BOLD,color.BLUE,now.strftime("%d/%m/%Y %H:%M:%S")," ",
      str(random.randrange(1000000, 9999999, 1)),color.END,'\n')
...
  print(color.BOLD,color.FAIL, "\nCould not find file in your Drive!\n" 
        ,color.END,color.WARNING," - Make sure you input the correct filename\n"
        ," - Make sure the file is saved in the google drive you mounted\n\n"
        ,color.END)
...
  print(color.BOLD,color.WARNING, "Exception Occured, Please Check Log"
  ,color.END)
...
  print(color.GREEN,"Conversion Complete!\nGreat Job and Have a Wonderful Day!",color.END,"\U0001F30C")
```

- Suppressed nbconvert to only errors
 - ```
!jupyter nbconvert --to pdf "{fileloc}" --log-level ERROR
```

- Added error Handling for the two most common Errors (Wrong filename,File Not in Drive)
 - Error, Type, Traceback are now saved into an as-needed created file ErrorLog.txt when an error or exception occurs
 - Suppressed error output for user and replaced with Solutions
 - ```
import sys
...
try:
  fileloc = loc[0]
except IndexError as error:
  print(color.BOLD,color.FAIL, "\nCould not find file in your Drive!\n" 
        ,color.END,color.WARNING," - Make sure you input the correct filename\n"
        ," - Make sure the file is saved in the google drive you mounted\n\n"
        ,color.END)
  Er = str('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                            sys.exc_info()[1],
                                            sys.exc_info()[2].tb_lineno))
  f = open("ErrorLog.txt","a+"); f.write(Er); f.close()
  sys.tracebacklimit=0
  sys.exit("Please Try Again") 
except Exception as exception:
  print(color.BOLD,color.WARNING, "Exception Occured, Please Check Log"
  ,color.END)
  Er = str('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                            sys.exc_info()[1],
                                            sys.exc_info()[2].tb_lineno))
  f = open("ErrorLog.txt","a+");f.write(Er);f.close()
  sys.tracebacklimit=0
  sys.exit("Please Try Again")
```


##1.3 (Alexandra Werth, 0555, 27 September 2020)

*Changes:*

- Added 

```
# watermark 
from datetime import datetime
import random 
now = datetime.now()
print('\n', now.strftime("%d/%m/%Y %H:%M:%S"), random.randrange(1000000, 9999999, 1))
```
to display the date and time of PDF creation and a random 7-digit number associated with the document.

##1.2 (Arvind Aradhya, 2116, 25 September 2020)

*Changes:*

- Added 

```
  >> outputsuppressed.txt
```
to all the lines that involve installs, so as to suppress the debug messages that are usually printed to console, from appearing on the console, and subsequently, appearing in the PDF. Shaves off about 10 pages. 
- Improved Version Log


##1.1 (Thomas Horning, 1248, 25 September 2020)

*Changes:*

- Added completion responses
```
!echo 'Finding file. This may take a minute or two depending on the size of your drive'
```
```
!echo "";echo "Conversion Complete. The pdf will be in the same location as your .ipynb file";echo "";echo "Have a Nice Day!"
```
- Added Version Control and Dev Notes in Markdown



##1.0 (Thomas Horning, 0001, 25 September 2020)
- <font size="5"> ***Document Genesis*** </font>

#Previous Versions
Please place the previous versions code in a markdown cell below when an Update is pushed to students

##Version 1.3

### 2020-10-18_1433
Saved by: Thomas Horning
```
###############################################################
#Version 1.3  <--- Please Update After change and pin revision when you save!
###############################################################

#This code converts an .ipynb file to a Tex based PDF and saves it in the Colab
#Notebook folder with the same filename.pdf

filename = 'Week5_UnitAnalysis_and_PlotSolarFlareData.ipynb' # Ex. 'Coding_Packet.ipynb'

from google.colab import drive
drive.mount('/content/gdrive', force_remount = True) # This is done first because we need a temporal delay between mounting and calling
#Install some dependences into the RUNTIME (is not local, needs to reinstall every Factory runtime)
!pip install IPython >> outputsuppressed.txt
!pip install Latex >> outputsuppressed.txt
!pip install pandoc >> outputsuppressed.txt
!pip install nbconvert >> outputsuppressed.txt
!pip install jupyter >> outputsuppressed.txt

#Well known Ubuntu Tex library
!apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended >> outputsuppressed.txt

# Searches the Google drive directory for the filename and gives back it's location
#(This accounts for Wildcards and Spaces in the directory names)
#Uses jupyter and nbconvert to convert the ipynb file to a Tex file, then into a
#pdf

!IFS=$'\n' #Sets the reader to only break at newlines instead of spaces,tabs,and newlines
!echo 'Finding file. This may take a minute or two depending on the size of your drive'
loc= !find '/content/gdrive' -name "{filename}"
fileloc = loc[0]
!jupyter nbconvert --to pdf "{fileloc}"

# watermark 
from datetime import datetime
import random 
now = datetime.now()
print('\n', now.strftime("%d/%m/%Y %H:%M:%S"), random.randrange(1000000, 9999999, 1))

# The PDF will be in the same folder as the original file
!echo "";echo "Conversion Complete. The pdf will be in the same location as your .ipynb file";echo "";echo "Have a Nice Day!"
```

## Version 1.1 


### Genesis
Saved by: Thomas Horning

```
#This code converts an .ipynb file to a Tex based PDF and saves it in the Colab
#Notebook folder with the same filename.pdf

filename = 'filename.ipynb' # Ex. 'Coding_Packet.ipynb'

from google.colab import drive
drive.mount('/content/gdrive', force_remount = True) # This is done first because we need a temporal delay between mounting and calling
#Install some dependences into the RUNTIME (is not local, needs to reinstall every Factory runtime)
!pip install IPython 
!pip install Latex 
!pip install pandoc
!pip install nbconvert
!pip install jupyter

#Well known Ubuntu Tex library
!apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended

# Searches the Google drive directory for the filename and gives back it's location
#(This accounts for Wildcards and Spaces in the directory names)
#Uses jupyter and nbconvert to convert the ipynb file to a Tex file, then into a
#pdf

!IFS=$'\n' #Sets the reader to only break at newlines instead of spaces,tabs,and newlines
!echo 'Finding file. This may take a minute or two depending on the size of your drive'
loc= !find '/content/gdrive' -name "{filename}"
fileloc = loc[0]
!jupyter nbconvert --to pdf "{fileloc}"

```

