import os.path
import sys
from pathlib import Path

def genwoid():
    woid = 1
    filename = os.getcwd() + "\\" + str(woid) + ".txt"
    filepath = Path(filename)
    while filepath.exists():
        woid += 1
        filename = os.getcwd() + "\\" + str(woid) + ".txt"
        filepath = Path(filename)
    return filepath
    
def newwo():
    fields = ["Name","Mobile","Landline","Email","Address","Type(Laptop/Mobile/Tablet/Printer)","Make","Model","Serial","Issue","Password"]
    with open(genwoid(),"wt") as f:
        for field in fields:
            f.write(field+": "+input(field+": ")+"\n")


def updatewo(woid):
    with open(str(woid)+".txt","at") as f:
        status = input("Please input status as number between 1 and 4.\n\t0)Waiting for bench.\n\t1)In Progress\n\t2)On Hold\n\t3)Ready\n\t4)Checked Out\n\t5)Ambandoned\n:>>")
        note = input("Please add note:\n")

        update = "\nStatus: "+status+"\nNote:\n"+"-"*5+"\n"+note

        f.write("\n"+"="*24+update+"\n" + "="*24+"\n")

def main(argv):
    if argv[0] == 'new':
        newwo()
    if argv[0] == 'update':
        updatewo(argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
    
