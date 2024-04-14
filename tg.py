"""
Training Grounds: This is where I can go off to the side and test out snippets of code.

Firstly, I think the program would work better if I rearrange it. Instead of starting off with the login() function,
we should incorporate it within the main body of the program.

For today's goal, let's work on downloading multiple reports and then saving the filepaths for each as items in a list.
DONE!
Next, We will go through and refactor the code to work together more cohesively - In Progress
"""

from funcs import *

# 'course_id' variable will eventually be user-defined. It is only static now for testing purposes.
# We will use the web interface to set the variable
course_id = ["7437580", "4673600", "4673603"]
# Master report name will remain fixed.
master_report = "masterrr.xlsx"

# Additions: Select which course to work with (Can be selected on website). - NOT DONE
# Also add option to run all reports at once. This will be done in the web interface - NOT DONE

print("Note: everything printed in the terminal is for dev-testing only. Please ignore, as it will be deleted later")
# Begin main body of program-----
# Log in and build a list of filepaths for all the reports we just downloaded.
reports = login(course_id)
print(f"Here is your dictionary: {reports}")
course_name = []

for num in course_id:
    course_name.append(courses[num])

print(course_id)
print(course_name)
# Check for existence of master file and proceed accordingly
if os.path.exists(master_report):
    print("Report exists")
    # If it exists: open it and check to see if a sheet exists for the selected course name.
    master = openpyxl.load_workbook(master_report)
    for title in course_name:
        # If sheet exists: select sheet, transfer data from downloaded file, and format
        if title in master.sheetnames:
            print("Sheet exists")
            master.active = master[title]
            ws = master.active
            report = courses[title]
            convert(report, ws)
            fix(ws)
        # If not: create the sheet, transfer data from downloaded file, and format
        else:
            print("Sheet doesn't exist yet")
            master.create_sheet(title)
            master.active = master[title]
            ws = master.active
            report = courses[title]
            convert(report, ws)
            fix(ws)
# If Master File does not exist: Create a new workbook and sheets, transfer data, and format
else:
    master = openpyxl.Workbook()
    for title in course_name:
        master.create_sheet(title)
        master.active = master[title]
        ws = master.active
        cid = {i for i in courses if courses[i] == title}
        print(reports[cid])
        # print(report)
        # # report = courses[title]
        # convert(report, ws)
        # fix(ws)

# Save our work and close the file
save_path = f"C:/Users/danny/Project/{master_report}"
master.save(save_path)
master.close()

# Open and view the master file that we just finished working with.
os.system(f"start EXCEL.EXE {save_path}")
