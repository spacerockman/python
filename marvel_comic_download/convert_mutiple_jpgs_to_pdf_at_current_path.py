from fpdf import FPDF
import os
import sys
import natsort

dir_name = sys.path[0]
curr_directory_name = dir_name.split("/")[-1]

pdf = FPDF()
pdf.set_auto_page_break(0)
files_list = []
jpg_files = os.listdir(dir_name)
for i in jpg_files:
    if i.endswith('.jpg'):
        files_list.append(i)

# sored files by name
file_list = natsort.natsorted(files_list)

# show the order
for i in file_list:
    print(i)

# imagelist is the list with all image filenames
for image in file_list:
    pdf.add_page()
    pdf.image(f"{dir_name}/{image}", w=190)
    pdf.output(f"{dir_name}/{curr_directory_name}.pdf", "F")
