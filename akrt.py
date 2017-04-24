import os.path #use for getcwd
import sys # for arguments 
from pathlib import Path # for checking a file already exists. Requires 3.6.1
import time # to get current datetime for reports
from flask import Flask, render_template #to host and render webpages from text files

app = Flask(__name__) #creates a flask object from the name of the script - akrt

def genwoid():
    """ Creates path to the next available woid """
    woid = 1 # define first possible woid
    filename = os.getcwd() + "\\" + str(woid) + ".txt" 
    filepath = Path(filename)  
    while filepath.exists():
        woid += 1
        filename = os.getcwd() + "\\" + str(woid) + ".txt"
        filepath = Path(filename)
    return filepath

# list of status numbers and corresponding meanings
statuses = {0:'Waiting for Bench',1:'In Progress',2:'On Hold',3:'Ready',4:'Checked Out',5:'Ambandoned'}
    
def newwo():
    """ Creates new work order text file from list of fields as well as book in time """
    fields = ["Name","Mobile","Landline","Email","Address","Type(Laptop/Mobile/Tablet/Printer)","Make","Model","Serial","Issue","Deadline(HH:MM:DD:MM:YY):"]
    with open(genwoid(),"wt") as f:
        f.write("Booked In: "+time.strftime("%c")+"\n")
        for field in fields:
            f.write(field+": "+input(field+": ")+"\n")


def updatewo(woid):
    with open(str(woid)+".txt","at") as f:
        """ Adds a status with note on the current repair """
        status = input("Please input status as number between 1 and 4.\n\t0)Waiting for bench.\n\t1)In Progress\n\t2)On Hold\n\t3)Ready\n\t4)Checked Out\n\t5)Ambandoned\n:>>")
        note = input("Please add note:\n")

        update = "\n"+time.strftime("%c")+"\nStatus: "+status+"\nNote:\n"+"-"*5+"\n"+note

        f.write("\n"+"="*24+update+"\n" + "="*24+"\n")

        print("Work Order "+woid+" successfully updated")

def getwo(woid):
    with open(str(woid)+".txt","rt") as f:
        """ Returns a string from a work order text file """
        values = f.read()
    return values

def getstatus(woid):
    """ Returns a repair status number from getwo's string """
    values = getwo(woid).split("\n")
    for line in values:
        if line.split(":")[0]=="Status":
            return line.split(":")[1]
        else:
            return 0


@app.route("/report/<int:woid>") 
def webreport(woid):
    """ Generates report.html page from woid enter in address bar """
    status = statuses[int(getstatus(woid))] # get status in textual form
    return render_template('report.html', status=status)


@app.route("/")
def index():
    """ Returns text telling customer how to use web interface """
    return "Usage: {domain}/report/<woid>" 

def main(argv):
    """ Checks arguments and handles exception if too many or too few arguments are passed """

    usage = "Usage:\n"+"-"*6 + "\nakrt.py new - launch new ticket,\nakrt.py update [woid] - update previous ticket\nakrt.py about [woid] - read ticket file \nakrt.py daemon - launch web server"
    try:
        if argv[0] == 'new':
            newwo() # create a new work order
        elif argv[0] == 'update':
            updatewo(argv[1]) # update the work order under the next parameter
        elif argv[0] == 'daemon':
            app.run() # run the flask web server
        elif argv[0] == 'about':
            print(getwo(argv[1])) # prints out the contents of a work order 
        else:
            print(usage)
    except IndexError:
        print(usage)

# runs main first if script is module is being run standalone.
if __name__ == "__main__":
    main(sys.argv[1:])

