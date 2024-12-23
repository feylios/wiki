# builds a html file that shows all of the files on the site
import os, os.path, markdown

# open the file
directory = "C:/Users/joshm/Documents/Feylios/wiki/"
website = "https://feylios.github.io/wiki"
file = open(directory + "index.html", "w")
# write our file header
file.write("<h1>Files</h1>")

# scan a directory and write the files
def scanDirectory(cdir, h):
    # get a list of all our files
    dir_list = os.listdir(cdir)
    # loop through the files, and ignore .git, .py, and the index.html file
    for x in dir_list:
        ## x is our string filename
        if ".git" in x or ".py" in x or "index.html" in x or "files.html" in x or "CNAME" in x or ".css" in x or "vault" in x or "styles" in x: 
            continue
        ## if the file is a folder, scan that folder
        if "." not in x:
            ## write a header for the folder
            writeHeader(x, h)
            ## then scan
            scanDirectory(cdir + "/" + x, h + 1)
            continue
        ## otherwise, write the file name to the document
        writeLine(x, cdir, h)
        ## if a file name contains a space, then send a warning
        if " " in x:
            print("WARNING! Space detected in file name: " + x)

def writeHeader(text, h):
    line = "<h" + str(h) + ">" + text + "</h"+ str(h) +">"
    file.write(line)

def writeLine(text, dir, h):
    ## get our web directory by removing the directory from the dir and adding the website
    dir = dir.removeprefix(directory)
    dir = dir + "/" + text
    print(dir)
    wdir = website + dir
    print(wdir)
    ## print(wdir)
    line = '<a href="' + wdir + '">' + text + '</a>' + '<br>'
    file.write(line)

scanDirectory(directory,1)

file.close()
# write lines to a file