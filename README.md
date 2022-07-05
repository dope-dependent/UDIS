# UDIS
University Department Information System (UDIS) is a Python based GUI application to store, update and modify various academic and administrative records of a University Department. 

## Languages and Frameworks Used
This application uses `Python` for coding purposes, `Tkinter` library of `Python` to design the GUI and `SQLite3` to manage data

# Modes of Operation
### Normal Utility Mode
This mode has been made to run the application for normal everyday usage, without an explicit need for testing  
To use the application in this mode, simply run the `Main.py` file

#### **First Run**
1. On the first run of the application, make sure that there is no `UDIS.db` present in the `Backend` folder
2. Set the credentials when prompted

**You cannot proceed further without setting the credentials**

#### **Subsequent Runs**
Enter the credentials to login to the system and use it as desired

### Test Mode
To test the application, create a new `UDIS.db` file in the `Backend` folder and run all the `SQL` queries present in the `BuildDB.txt` file. Now, run the `Test.py` file and redirect output to any text file or console as desired.


## Contibutors
This application has been created by the joint collaboration of [Nikhil Tudaha](https://github.com/nikhiltudaha), [Seemant G. Achari](https://github.com/pasthorizon) and [me](https://github.com/dope-dependent).
