################################################################################
#                    CODE TO CONVERT COLAB NOTEBOOK TO PDF                     #
#This code converts an .ipynb file to a Tex based PDF and saves it in the Colab#
#Notebook folder with the same filename.pdf                                    #
################################################################################
# Function List 
################################################################################

#Converter for .ipynb conversion to PDF. Input is a string of the file name

def find(name, path):
    import os
    class color:
        BLUE = '\033[94m';
        GREEN = '\033[92m';
        BOLD = '\033[1m';
        UNDERLINE = '\033[4m';
        END = '\033[0m';
        FAIL = '\033[91m';
        WARNING = '\033[93m';
    for root, dirs, files in os.walk(path):
      if name in files:
        return os.path.join(root, name)

def PDFconvertGC(filename):
    # Imports
    from google.colab import drive; from datetime import datetime; import sys; 
    import os; import time;
    class color:
        BLUE = '\033[94m';
        GREEN = '\033[92m';
        BOLD = '\033[1m';
        UNDERLINE = '\033[4m';
        END = '\033[0m';
        FAIL = '\033[91m';
        WARNING = '\033[93m';
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
    os.system('apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended --fix-missing >> outputsuppressed.txt')
    os.system('apt-get update >> outputsuppressed.txt')
    # Searches the Google drive directory for the filename and gives back it's 
    # location (This accounts for Wildcards and Spaces in the directory names).
    # Uses jupyter and nbconvert to convert to a Tex file, then into a pdf 
    # Handle Common Errors
    print('\nFinding file. This may take a minute or two depending on the size of your drive...')
    os.system("IFS=$'\n'") #Sets the reader to only break at newlines instead of spaces, tabs,and newline
    try:
      loc = find(filename, '/content/gdrive')
      if str(loc) == "None":
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
      else:
        print('File Found at: ',str(loc))   
    except Exception as exception:
        print(color.BOLD,color.WARNING, "Exception Occured, Please Check Log",color.END)
        Er = str('Error: {}. {}, line: {}'.format(sys.exc_info()[0],sys.exc_info()[1]
                                          ,sys.exc_info()[2].tb_lineno))
        f = open("ErrorLog.txt","a+");f.write(Er);f.close()
        sys.tracebacklimit=0
        sys.exit("Please Try Again")
   # Autosave file
    !sleep 30s
   # Convert the file
    !jupyter nbconvert --output-dir='./content/' --to pdf {loc} --log-level ERROR
    # The PDF will be in the same folder as the original file
    print(color.GREEN,"Conversion Complete!\nThe PDF is in the Contents folder.\nGreat Job and Have a Wonderful Day!"
            ,color.END,"\U0001F30C")
    t4 = time.time(); 
    m = str(int((t4-t1)/60)); 
    s = str(int((t4-t1)% 60))
    print("Total Time: ",m," m  ",s," s")
    
def Watermark(filename):
    from datetime import datetime; import random;
    # To make Watermark distinctive
    class color:
        BLUE = '\033[94m';
        GREEN = '\033[92m';
        BOLD = '\033[1m';
        UNDERLINE = '\033[4m';
        END = '\033[0m';
        FAIL = '\033[91m';
        WARNING = '\033[93m';

     # Make Watermark
    now = datetime.now()
    print(color.UNDERLINE,'Unique Watermark',color.END)
    print(color.BOLD,color.BLUE, str(filename),'\U0001F512',color.END)
    print(color.BOLD,color.BLUE,now.strftime("%d/%m/%Y %H:%M:%S")," "
            ,str(random.randrange(1000000, 9999999, 1)),color.END,'\n')
