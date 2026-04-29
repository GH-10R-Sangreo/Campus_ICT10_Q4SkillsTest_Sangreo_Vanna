from pyscript import display, document
import numpy as np

import matplotlib.pyplot as plt
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close

# CLASSMATES LIST
class Classmate:
    def __init__(self, name, section, fav_subject):
        self.name = name
        self.section = section
        self.fav_subject = fav_subject
        document.getElementById('output').innerHTML = ' '

    def introduce(self):
        display(f'Hi! I am {self.name} from {self.section}. My favorite subject is {self.fav_subject}.')


classmates_list = [
    Classmate('Cerinne Olmedo', 'Ruby', 'Math'),
    Classmate('Tarcisius Cañete', 'Ruby', 'PE'),
    Classmate('Charlize Galang', 'Ruby', 'English'),
    Classmate('Aisha Ledesma', 'Ruby', 'Science'),
    Classmate('Kaitlyn Nardo', 'Ruby', 'Social Studies'),
]


def add_classmate(e):
    name = document.getElementById('name1').value
    section = document.getElementById('section1').value
    subject = document.getElementById('subject1').value

    if name and section and subject:
        new_classmate = Classmate(name, section, subject)
        classmates_list.append(new_classmate)

    document.getElementById('name1').value = ''
    document.getElementById('section1').value = ''
    document.getElementById('subject1').value = ''

    display(f'Classmate added successfully!', target='output')


def show(e):
    document.getElementById('output').innerHTML = ' '

    for classmate in classmates_list:
        classmate.introduce()

# ATTENDANCE CHECKER
def checkAttendance(e):
    plt.clf()
    plt.show()
    plt.title('Attendance Checker')
    plt.xlabel('Days')
    plt.ylabel('Absences')
    Monday = float(document.getElementById('monday').value)
    Tuesday = float(document.getElementById('tuesday').value)
    Wednesday = float(document.getElementById('wednesday').value)
    Thursday = float(document.getElementById('thursday').value)
    Friday = float(document.getElementById('friday').value)
    days = np.array([Monday, Tuesday, Wednesday, Thursday, Friday])
    numberAbsences = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
    attendance_graph = plt.plot(numberAbsences, days)

# PHOTOS OF CLASS ACTIVITIES