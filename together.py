"""This program is designed to navigate to and log into specific webpages of the Schoox training website and download
reports for various training modules. Afterward, it will take the newly-downloaded .csv file, and format into a
corporate-friendly .xlsx file for manager use. It is the intention of the developer to add further functionality to this
program in the future.
"""
# THIS PART OF THE PROJECT IS DONE, FOR NOW.
# This dictionary is here for testing purposes only
from funcs import *
courses = {
    "3846202": "NYS Intro",
    "3847508": "Anti-Harassment 1",
    "3846909": "Anti-Harassment 5",
    "3846758": "Anti-Harassment 6",
    "3848048": "Understanding Harassment 1",
    "3848322": "Understanding Harassment 2",
    "3848379": "Understanding Harassment 3",
    "3847029": "Understanding Harassment 4",
    "3846770": "Understanding Harassment: 05",
    "3848626": "Understanding Harassment 6",
    "3848445": "Understanding Harassment 7",
    "4775856": "NYS Scenarios",
    "4673600": "NYC Intro",
    "4673603": "NYC Scenarios",
    "7437580": "Menu Update"
}
# 'course_id' variable will eventually be user-defined. It is only static now for testing purposes.
course_id = ["7437580", "4673600", "4673603"]
master_report = "masterrr.xlsx"
# report = "creport.csv"  # Replace with "select_file()"


# Function to navigate to webpage, login, and download report. - FINISHED
# Additions: Select which course to work with (Can be selected on website). - NOT DONE
# Also add option to run all reports at once (look into running Selenium in the background). - NOT DONE

#----------------------------------------------------TESTING AREA-------------------------------------------------------

# reports = login(course_id)# User submitted id/pass? - MAYBE
# print(reports)
# for thing in reports:
#     os.system(f"start EXCEL.EXE {thing}")

#------------------------------------------------END TESTING AREA-------------------------------------------------------

# Set most recently downloaded file as a variable. This is necessary because the file downloads with a different name
# each time. - FINISHED
# Enhancement - We will instead have the "file" variable be a list of filepaths, so that we can work with multiple
# reports at once. This change will be made in the "funcs.py" file, instead of here. - IN PROGRESS
# file = select_file()

# --------------------BEGIN COMMENT
# Begin main body of program-----

login(course_id)

# Addition: Delete .csv file after we finish working with it! -  DONE
course_name = tab_save(course_id)
# Check for existence of master file and proceed accordingly
if os.path.exists(master_report):
    print("Report exists")
    master = openpyxl.load_workbook(master_report)
    if course_name in master.sheetnames:
        print("Sheet exists")
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
        if len(str(cell.cid)) > setlen:
            setlen = len(str(cell.cid))
            # This line is for testing only and can be deleted later.
            # print(f"The value of {cell} is {cell.value}, and the setlen is \'{setlen}\'")
            ws.column_dimensions[column].width = setlen + 2

# Bold and center the first row
for cell in ws["1:1"]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal="center")

# Save our work and close the file
save_path = f"C:/Users/danny/Project/{master_report}"
master.save(save_path)
master.close()


# Open and view the master file that we just finished working with.
os.system(f"start EXCEL.EXE {save_path}")
#--------------------END COMMENT-------------