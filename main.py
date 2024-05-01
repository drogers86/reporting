"""This program is designed to navigate to and log into specific webpages of the Schoox training website and download
reports for various training modules. Afterward, it will take the newly-downloaded .csv file, and format into a
corporate-friendly .xlsx file for manager use. It is the intention of the developer to add further functionality to this
program in the future.

This specific file is designed to be run in the terminal, and is not the final version of the program. It is being kept
for legacy purposes only.
"""

# Current as of 4/30/24

from funcs import *

# 'course_id' variable will eventually be user-defined. It is only static now for testing purposes.
# We will use the web interface to set the variable
course_id = ["7437580", "7437443"]
# Master report name will remain fixed.
master_report = "master.xlsx"

# Additions: Select which course to work with (Can be selected on website). - NOT DONE
# Also add option to run all reports at once. This will be done in the web interface - NOT DONE

print("Note: everything printed in the terminal is for dev-testing only. Please ignore, as it will be deleted later")
# Begin main body of program-----
# Log in and build a list of filepaths for all the reports we just downloaded.
reports = login(course_id)
course_name = []
cid = []

for num in course_id:
    course_name.append(courses[num])

# Check for existence of master file and proceed accordingly
if os.path.exists(master_report):
    # If it exists: open it and check to see if a sheet exists for the selected course name.
    master = openpyxl.load_workbook(master_report)
    for cid in course_id:
        title = courses[cid]
        # If sheet exists: select sheet, transfer data from downloaded file, and format
        if title in master.sheetnames:
            master.active = master[title]
            ws = master.active
            report = reports[cid]
            convert(report, ws)
            fix(ws)
        # If not: create the sheet, transfer data from downloaded file, and format
        else:
            master.create_sheet(title)
            master.active = master[title]
            ws = master.active
            report = reports[cid]
            convert(report, ws)
            fix(ws)
# If Master File does not exist: Create a new workbook and sheets, transfer data, and format
else:
    master = openpyxl.Workbook()
    for cid in course_id:
        title = courses[cid]
        master.create_sheet(title)
        master.active = master[title]
        ws = master.active
        report = reports[cid]
        convert(report, ws)
        fix(ws)

# Save our work and close the file
save_path = f"C:/Users/danny/Project/{master_report}"
master.save(save_path)
master.close()

# Open and view the master file that we just finished working with.
os.system(f"start EXCEL.EXE {save_path}")
