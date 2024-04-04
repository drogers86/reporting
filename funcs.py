import time, os, csv, openpyxl
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)


# options = chrome_options

def login(course_id):
    driver = webdriver.Chrome(options = chrome_options)
    user = "102026939"
    passw = "RedLobster1"

    # Login
    driver.get(
        f"https://app.schoox.com/academies/panel/dashboard2/training/course.php?acadId=7592&course_id={course_id}")
    time.sleep(.25)
    driver.find_element("xpath", "//*[@id='main']/div/main/input[6]").send_keys(user)
    driver.find_element("xpath", "//*[@id='main']/div/main/input[7]").send_keys(passw)
    button_1 = driver.find_element("name", "button")
    button_1.click()

    # Download report
    time.sleep(2)
    button_2 = driver.find_element("xpath", "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/img")
    button_2.click()
    button_3 = driver.find_element("xpath",
                                   "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/p[1]/a/span/span")
    button_3.click()
    time.sleep(1)
    button_4 = driver.find_element("xpath", "/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/generate-report/div/div/p/a")
    button_4.click()
    time.sleep(1)


# Select most recently downloaded file
def select_file():
    directory_path = "C:/Users/danny/Downloads/"
    most_recent_file = None
    most_recent_time = 0

    for entry in os.scandir(directory_path):
        if entry.is_file():
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                most_recent_file = entry.name
                most_recent_time = mod_time
    file = f"{directory_path}{most_recent_file}"
    return file


# This function simply converts the .csv file to an .xlsx file
def convert(report, ws):
    with open(report) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                if row[6] == "0" or row[6] == "% Completed":
                    ws.append(row)
            except UnicodeDecodeError:
                pass
            except IndexError:
                continue
        f.close()


"""
# Here, we check to see if our master file exists. If so, we then check to see if the sheet we want exists. If so, 
# we then use the "convert" function to iterate through each row and save only the ones we want to our master file. 
# If either of the two conditions are untrue, they are first created (the master file, or the sheet for the report 
# that we're working with) and then the "convert" function is applied. - FINISHED
"""


# This actually might end up being the main body of my program, lol
# def delete_convert_move(master_report, report, course_id):
    # course_name = tab_save(course_id)
    # # Check for existence of master file and proceed accordingly
    # if os.path.exists(master_report):
    #     master = openpyxl.load_workbook(master_report)
    #     if course_name in master.sheetnames:
    #         master.active = master[course_name]
    #         ws = master.active
    #         convert(report, ws)
    #     else:
    #         master.create_sheet(course_name)
    #         master.active = master[course_name]
    #         ws = master.active
    #         convert(report, ws)
    # else:
    #     master = openpyxl.Workbook()
    #     master.create_sheet(course_name)
    #     master.active = master[course_name]
    #     ws = master.active
    #     convert(report, ws)
    #
    # # Delete unwanted columns
    # ws.delete_cols(idx=4, amount=3)
    # ws.delete_cols(idx=5, amount=5)
    #
    # # Auto-width columns
    # for col in ws.columns:
    #     setlen = 0
    #     column = col[0].column_letter
    #     # This line is for testing only and can be deleted later.
    #     print(f"You are in Column:{column}")
    #     for cell in col:
    #         if len(str(cell.value)) > setlen:
    #             setlen = len(str(cell.value))
    #             # This line is for testing only and can be deleted later.
    #             print(f"The value of {cell} is {cell.value}, and the setlen is \'{setlen}\'")
    #             ws.column_dimensions[column].width = setlen + 2
    #
    # # Bold and center the first row
    # for cell in ws["1:1"]:
    #     cell.font = Font(bold=True)
    #     cell.alignment = Alignment(horizontal="center")
    #
    # # Save our work and close the file
    # save_path = f"D:/School/Spring_2024/Python/CISS100/{master_report}"
    # master.save(save_path)
    # master.close()
    # return [ws, save_path]  # 86


# This function will define which tab to save our work to based on the course id number
def tab_save(course_id):
    # Here, we identify all the possible course ids that we will be working with. Right now it's just a dictionary,
    # but I'm planning to add to it later.
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
        "7437580": "Menu Update",
        "1": "Sheet1",
        "2": "Sheet2",
        "3": "poo",
        "4": "Sheet3",
        "5": "Sheet6",
        "6": "stuff",
        "7": "Sheet4",
        "8": "Sheet6",
    }
    course_name = courses[course_id]
    return course_name

# Next------

