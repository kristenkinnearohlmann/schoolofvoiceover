# File: Check for empty directories
# Author: Kristen Kinnear-Ohlmann
# URL: kristenkinnearohlmann.com
# Version: 1.0.0.0

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import os

global check_path
global empty_dirs

def main():
    root = tk.Tk()
    root.withdraw() # close the root window

    directory_path() # select path to check
    msg.showinfo("Selected Path","Here is the path to check: " + check_path)

    check_dirs() # check directories
    msg.showinfo("Empty Directories","The empty directories are:\n\n" + '\n'.join(empty_dirs))

def directory_path():
    global check_path

    msg.showinfo("Select Path to Check", "Select the path to check expo attendee directories.")
    check_path = fd.askdirectory(initialdir = "/",title="Select Path to Check for Directories")

def check_dirs():
    global empty_dirs
    empty_dirs = []
    
    for dirpath, dirnames, files in os.walk(check_path):
        if files:
            continue
        if not files:
            empty_dirs.append(dirpath[dirpath.find("\\")+1:len(dirpath)])


# run the program
main()