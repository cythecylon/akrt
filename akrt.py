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
    
