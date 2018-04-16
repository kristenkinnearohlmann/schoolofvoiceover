# File: Move Expo Files
# Author: Kristen Kinnear-Ohlmann
# URL: kristenkinnearohlmann.com
# Version: 1.0.0.0

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import os
import shutil
from shutil import copyfile as cp
from shutil import move as mv

global source_path
global output_path

def main():
    root = tk.Tk()
    root.withdraw() # close the root window

    get_source_path() # retrieve file with attendees
    get_output_path() # select output path
    msg.showinfo("Selected Directories","Here are the selected directories: \n\nSource Directory: " + source_path + "\n\n" + "Output Directory: " + output_path)

    move_files() # create directories from list to path
    os.startfile(output_path)

def get_source_path():
    global source_path

    msg.showinfo("Select Expo Audio", "Select the folder containing expo audio.")
    source_path = fd.askdirectory(initialdir = "/",title="Select Expo Audio Directory")

def get_output_path():
    global output_path

    msg.showinfo("Select Output Path", "Select the path to output expo attendee directories.")
    output_path = fd.askdirectory(initialdir = "/",title="Select Output Path for Directories")

def move_files():
    amp_char_pos = 0
    uscore_char_pos = 0
    person1 = ""
    person2 = ""

    for filename in os.listdir(source_path):
        if filename.endswith(".mp3"):
            if filename.find("&") > 0: # doubles
                amp_char_pos = filename.find("&")
                uscore_char_pos = filename.find("_")
                person1 = filename[:amp_char_pos]
                person2 = filename[amp_char_pos+1:uscore_char_pos]

                # copy to person 1
                if not os.path.exists(output_path + "/" + person1):
                    os.makedirs(output_path + "/" + person1)
                cp(source_path + "/" + filename,output_path + "/" + person1 + "/" + filename)

                # move to person 2
                if not os.path.exists(output_path + "/" + person2):
                    os.makedirs(output_path + "/" + person2)
                mv(source_path + "/" + filename,output_path + "/" + person2 + "/" + filename)

            else: # singles
                uscore_char_pos = filename.find("_")
                person1 = filename[:uscore_char_pos]

                # move to person 1
                if not os.path.exists(output_path + "/" + person1):
                    os.makedirs(output_path + "/" + person1)
                mv(source_path + "/" + filename,output_path + "/" + person1 + "/" + filename)

# run the program
main()