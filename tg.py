"""
Training Grounds: This is where I can go off to the side and test out snippets of code.

Firstly, I think the program would work better if I rearrange it. Instead of starting off with the login() function,
we should incorporate it within the main body of the program.


For today, let's come up with a way to loop through and work with multiple reports!
Steps:
1) Check for file
2) If no file, loop through all reports.
"""

# Here, we will test using selenium to visit more than one page. We may have to break the function up.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
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

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
master_report = "masterrr.xlsx"
ids = ["3846202", "3847508"]

# options = chrome_options


def login_2(course_id): # THIS FUNCTION WORKS THE WAY I WANT IT TO.
    driver = webdriver.Chrome(options = chrome_options)
    course_id = course_id
    user = "102026939"
    passw = "RedLobster1"
    driver.implicitly_wait(2)

    # Login
    driver.get("https://app.schoox.com/login.php")
    driver.find_element("xpath", "//*[@id='main']/div/main/input[6]").send_keys(user)
    driver.find_element("xpath", "//*[@id='main']/div/main/input[7]").send_keys(passw)
    button_1 = driver.find_element("name", "button")
    button_1.click()

    for cid in course_id:
        url = f"https://app.schoox.com/academies/panel/dashboard2/training/course.php?acadId=7592&course_id={cid}"
        # Download report
        driver.get(url)
        button_2 = driver.find_element("xpath", "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/img")
        button_2.click()
        button_3 = driver.find_element("xpath","/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/p[1]/a/span/span")
        button_3.click()
        button_4 = driver.find_element("xpath", "/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/generate-report/div/div/p/a")
        button_4.click()

# ------------------------------------------------------BEGIN TEST------------------------------------------------------
"""
This bit of code (test() and test_2() ) is the foundation of how I want to visit multiple pages with selenium. The function will first accept 
a list of course ids as input. Then, it will iterate through that list and use each list item to complete a url. 
Finally, selenium will visit each page.
"""
# This function accepts a list as a parameter and then works with each item in the list separately
def test(courses):
    courses = courses
    urls = []
    # Build "url" actions
    for cid in courses:
        urls.append(f"www.{cid}.com")
    print(urls)


# This function just proves that I can accept a list as a parameter. NBD.
def test_2(links):
    links = links
    print(links)

# links = ["Google", "Yahoo", "AOL"]

# test_2(links)
# print("-------------------------------------------------------------------------------------------------------------")
# test(links)

# ---------------------------------------------------END TEST-----------------------------------------------------------

links = ["7437580", "7437443"]
login_2(links)



# This bit checks to see if our master file exists. If not, it will create a new workbook with course IDs as sheets
# if os.path.exists(master_report):
#     print("Exists")
#     # master = openpyxl.load_workbook(master_report)
#     # if course_name in master.sheetnames:
#     #     master.active = master[course_name]
#     #     ws = master.active
#     #     report = select_file()
#     #     convert(report, ws)
# else:
#     print("Nope")
#     master = openpyxl.Workbook()
#     for key in courses:
#         master.create_sheet(key)
#         # master.active = master[key]
#         # ws = master.active
#         # report = select_file()
#         # convert(report, ws)
#
# save_path = f"C:/Users/danny/Project/{master_report}"
# master.save(save_path)
# master.close()
# os.system(f"start EXCEL.EXE {save_path}")
