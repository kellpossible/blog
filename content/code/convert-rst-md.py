import os
import re

def convert_file(fname):
    print(fname)
    with open(fname, "r") as f:
        rst_lines = f.readlines()
    
    metadata_lines = []

    # metadata_lines.append(":title: " + lines[0])

    basename = os.path.splitext(fname)[0]
    editname = basename + ".tmp.rst"
    mdname =  basename + ".md"

    with open(editname, "w") as f:
        for line in rst_lines:
            if len(re.findall(r"^[:]\w+[:]", line)) > 0:
                metadata_lines.append(line)
            else:
                f.write(line)

    print(metadata_lines)
    toml_metadata_lines = to_toml_metadata(metadata_lines)
    print(toml_metadata_lines)

    command = "pandoc {0} -t commonmark -o {1}".format(editname, mdname)
    os.system(command)

    os.remove(editname)

    with open(mdname, "r") as f:
        md_lines = f.readlines()

    with open(mdname, "w") as f:
        f.write("+++\n")
        for line in toml_metadata_lines:
            f.write(line)
        f.write("+++\n\n")
        
        for line in md_lines:
            f.write(line)

    # os.remove(mdname)

def to_toml_metadata(rst_lines):
    toml_lines = []

    for line in rst_lines:
        line = line.strip('\n')
        m = re.match(r"^[:](\w+)[:] (.*)", line)
        g = m.groups()
        key = g[0]
        value = g[1]

        format_string = "{0} = \"{1}\""
        
        if key == "date":
            format_string = "{0} = {1}"
            value = re.findall("\d{4}-\d{2}-\d{2}", value)[0]

        toml_lines.append(format_string.format(key, value) + "\n")

    return toml_lines
            

def convert_files():
    for file in os.listdir("."):
        if file.endswith(".rst"):
            fname = os.path.join("./", file)

            convert_file(fname)

if __name__ == "__main__":
    convert_files()