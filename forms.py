"""This is an experiment. I've noticed that I work with the course ID pretty often, so I'm trying to see if I can use
a class to tidy things up. This file is a dedicated space for me to experiment with making that work. Once I succeed
in doing that, I will refactor my main program to include the class."""


class Courses:
    def __init__(self, course_id, title, file):
        self.cid = course_id
        self.title = title
        self.titles = []
        self.file = file

    def titles(self, cid):
        print(cid)
        # for num in cid:
        #     print(num)
        # self.titles.append(self.cid[num])
        return self.titles


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
    "7437580": "Menu Update - FOH",
    "7437443": "Menu Update - BOH",
}
coursess = Courses([3846202, 3847508, 3847029], "poop", "c:/folder/file")
print(coursess.cid)
coursess.title()
