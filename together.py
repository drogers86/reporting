"""This program is designed to navigate to and log into specific webpages of the Schoox training website and download
reports for various training modules. Afterward, it will take the newly-downloaded .csv file, and format into a
corporate-friendly .xlsx file for manager use. It is the intention of the developer to add further functionality to this
program in the future.
"""
# THIS PART OF THE PROJECT IS DONE, FOR NOW.
from funcs import *

# 'course_id' variable will eventually be user-defined. It is only static now for testing purposes.
course_id = "7437580"
master_report = "masterrr.xlsx"
# report = "creport.csv"  # Replace with "select_file()"


# Function to navigate to webpage, login, and download report. - FINISHED
# Additions: Select which course to work with (Can be selected on website). - NOT DONE
# Also add option to run all reports at once (look into running Selenium in the background). - NOT DONE
login(course_id) # User submitted id/pass? - MAYBE

# Set most recently downloaded file as a variable. This is necessary because the file downloads with a different name
# each time. - FINISHED
file = select_file()

# Might not need this next section. -
# Convert to .xlsx with only the rows we want to keep and save to a different directory
# mws = delete_convert_move("masterrr.xlsx", "creport.csv", "3846909")

# Begin main body of program-----

# Addition: Delete .csv file after we finish working with it! - NOT DONE
# print(f"Welcome to my fancy-pants program!")
# input(f"What is the course id#? ")
course_name = tab_save(course_id)
# Check for existence of master file and proceed accordingly
if os.path.exists(master_report):
    master = openpyxl.load_workbook(master_report)
    if course_name in master.sheetnames:
        master.active = master[course_name]
        ws = master.active
        report = select_file()
        convert(report, ws)
    else:
        master.create_sheet(course_name)
        master.active = master[course_name]
        ws = master.active
        report = select_file()
        convert(report, ws)
else:
    master = openpyxl.Workbook()
    master.create_sheet(course_name)
    master.active = master[course_name]
    ws = master.active
    report = select_file()
    convert(report, ws)

# Delete unwanted columns
ws.delete_cols(idx=4, amount=3)
ws.delete_cols(idx=5, amount=5)

# Auto-width columns
# REMEMBER TO REMOVE THE CODE THAT PRINTS TEXT IN THE CONSOLE. IT IS FOR TESTING PURPOSES ONLY.
for col in ws.columns:
    setlen = 0
    column = col[0].column_letter
    # This line is for testing only and can be deleted later.
    # print(f"You are in Column:{column}")
    for cell in col:
        if len(str(cell.value)) > setlen:
            setlen = len(str(cell.value))
            # This line is for testing only and can be deleted later.
            # print(f"The value of {cell} is {cell.value}, and the setlen is \'{setlen}\'")
            ws.column_dimensions[column].width = setlen + 2

# Bold and center the first row
for cell in ws["1:1"]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal="center")

# Save our work and close the file
save_path = f"D:/School/Spring_2024/Python/CISS100/{master_report}"
master.save(save_path)
master.close()


# Open and view the master file that we just finished working with.
os.system(f"start EXCEL.EXE {save_path}")
