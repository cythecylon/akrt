import os.path
import sys
from pathlib import Path
import time
from flask import Flask, render_template

app = Flask(__name__)

def genwoid():
    woid = 1
    filename = os.getcwd() + "\\" + str(woid) + ".txt"
    filepath = Path(filename)
    while filepath.exists():
        woid += 1
        filename = os.getcwd() + "\\" + str(woid) + ".txt"
        filepath = Path(filename)
    return filepath

statuses = {0:'Waiting for Bench',1:'In Progress',2:'On Hold',3:'Ready',4:'Checked Out',5:'Ambandoned'}
    
def newwo():
    fields = ["Name","Mobile","Landline","Email","Address","Type(Laptop/Mobile/Tablet/Printer)","Make","Model","Serial","Issue","Deadline(HH:MM:DD:MM:YY):"]
    with open(genwoid(),"wt") as f:
        f.write("Booked In: "+time.strftime("%c")+"\n")
        for field in fields:
            f.write(field+": "+input(field+": ")+"\n")


def updatewo(woid):
    with open(str(woid)+".txt","at") as f:
        status = input("Please input status as number between 1 and 4.\n\t0)Waiting for bench.\n\t1)In Progress\n\t2)On Hold\n\t3)Ready\n\t4)Checked Out\n\t5)Ambandoned\n:>>")
        note = input("Please add note:\n")

        update = "\n"+time.strftime("%c")+"\nStatus: "+status+"\nNote:\n"+"-"*5+"\n"+note

        f.write("\n"+"="*24+update+"\n" + "="*24+"\n")

        print("Work Order "+woid+" successfully updated")

def getwo(woid):
    with open(str(woid)+".txt","rt") as f:
        values = f.read()
    return values

def getstatus(woid):
    values = getwo(woid).split("\n")
    for line in values:
        if line.split(":")[0]=="Status":
            return line.split(":")[1]
        else:
            return 0


@app.route("/report/<int:woid>")
def webreport(woid):
    status = statuses[int(getstatus(woid))]
    return render_template('report.html', status=status)


@app.route("/")
def index():
    return "Usage: {domain}/report/<woid>"

def main(argv):
    try:
        if argv[0] == 'new':
            newwo()
        if argv[0] == 'update':
            updatewo(argv[1])
        if argv[0] == 'daemon':
            app.run()
        if argv[0] == 'about':
            print(getwo(argv[1]))
    except IndexError:
        print("Usage:\n"+"-"*6 + "\nakrt.py new - launch new ticket,\nakrt.py update [ticketid] - update previous ticket\nakrt.py about [woid] - read ticket file \nakrt.py daemon - launch web server")

if __name__ == "__main__":
    main(sys.argv[1:])
   
