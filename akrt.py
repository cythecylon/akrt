import os.path
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
    fields = ["Name","Mobile","Landline","Email","Address","Make","Model","Serial","Issue","Password"]
    with open(genwoid(),"wt") as fin:
        for field in fields:
            fin.write(field+": "+input(field+": ")+"\n")


newwo()
