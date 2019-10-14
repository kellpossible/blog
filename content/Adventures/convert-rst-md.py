import os
import re

def convert_file(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    
    with open(fname, "w") as f:
        for line in lines:
            print(len(re.findall(r"^[:]\w+[:]", line)))
    



def convert_files():
    for file in os.listdir("."):
        if file.endswith(".rst"):
            fname = os.path.join("./", file)

            convert_file(fname)

if __name__ == "__main__":
    convert_files()