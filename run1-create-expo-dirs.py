# File: Create Expo Dirs
# Author: Kristen Kinnear-Ohlmann
# URL: kristenkinnearohlmann.com
# Version: 1.0.0.0

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import csv
import os

global input_file_path
global output_file_path

def main():
    root = tk.Tk()
    root.withdraw() # close the root window

    input_selection() # retrieve file with attendees
    output_path() # select output path
    msg.showinfo("Selected File and Path","Here are the selected file and output path: \n\nSource File: " + input_file_path + "\n\n" + "Output Path: " + output_file_path)

    create_dirs() # create directories from list to path
    os.startfile(output_file_path)

def input_selection():
    global input_file_path

    msg.showinfo("Select Expo Attendees", "Select the file containing expo attendee names.")
    input_file_path = fd.askopenfilename(initialdir = "/",title="Select Expo Attendees File",filetypes = (("csv files","*.csv"),("all files","*.*")))

def output_path():
    global output_file_path

    msg.showinfo("Select Output Path", "Select the path to output expo attendee directories.")
    output_file_path = fd.askdirectory(initialdir = "/",title="Select Output Path for Directories")

def create_dirs():
    csv_file = open(input_file_path,'rU')
    expo_reader = csv.reader(csv_file,delimiter=',')
    for row in expo_reader:
        row_data = row
        if row_data[0] != "username":
            folder_name = row_data[2] + row_data[3][:1]
            if not os.path.exists(output_file_path + "/" + folder_name):
                os.makedirs(output_file_path + "/" + folder_name)

# run the program
main()