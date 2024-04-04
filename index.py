"""
In this document, I will modify random functions to enable added functionality. This is a work in progress
"""

from funcs import *

old_report = "old_ssheet.xlsx"
file = "new_ssheet.xlsx"
# course_id = "6"

# Let's work with the "tab_save()"function to accept user input
course_id = input(f"What is the course id#? ")
name = tab_save(course_id)

print(name)
