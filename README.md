# SER-502-Team-10

Youtube video link : https://youtu.be/Ep-rQTH7Wtw

The requirements are : 
1) Prolog version 8.x or higher
2) Python version 3.5 or higher
3) Pyswip version : 0.2.9

We are using PySwip which will use virtual python environment.
The first requirement is to put all the files in /src folder.

The code (.marcel) should be in src directory as well.

Once in src folder, open the terminal and run the following.

1) python3 -m venv pyswip_env

2) For Linux :
source pyswip_env/bin/activate

For Windows:
pyswip_env\Scripts\activate


3) pip install pyswip
4) pip install nltk

5) Usually the below mentioned paths are already set but in case they are not please follow the following                 commands. Next export the path to swipl (SWISH Prolog) executable to PATH variable

6) Suppose swipl executable is in /Applications/SWI-Prolog.app/Contents/MacOS the the command would be :
    export PATH=$PATH:/Applications/SWI-Prolog.app/Contents/MacOS

7) Add the libswipl.dylib file path to DYLD_FALLBACK_LIBRARY_PATH variable. eg.
    export DYLD_FALLBACK_LIBRARY_PATH=/usr/local/Cellar/swi-prolog/8.0.3_1/libexec/lib/swipl/lib/x86_64-darwin

The libraries used are : https://github.com/yuce/pyswip/blob/master/INSTALL.md

--------------------------------
Once these steps are completed, within the src folder run the executable_file.py using command
    
        python executable_file.py

    This will prompt to enter the file name to be run (.marcel extension).
    Input the file name and press enter.

To deactivate the environment type command:
        deactivate

-----------------------------------
ALTERNATE RUNNING INSTRUCTIONS:

1.  run  ->  python3 -m venv pyswip_env

2. source pyswip_env/bin/activate

3. run the shellscript -> ./run.sh

4. Run the  python executable_file.py

5. This will prompt to enter the file name to be run (.marcel extension).
    Input the file name and press enter.
